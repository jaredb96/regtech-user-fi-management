from contextlib import asynccontextmanager
import os
import logging
from http import HTTPStatus
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from starlette.middleware.authentication import AuthenticationMiddleware
from alembic.config import Config
from alembic import command

from regtech_api_commons.oauth2.oauth2_backend import BearerTokenAuthBackend
from regtech_api_commons.oauth2.oauth2_admin import OAuth2Admin
from regtech_api_commons.api.exceptions import RegTechHttpException
from regtech_api_commons.api.exception_handlers import regtech_http_exception_handler, request_validation_error_handler

from regtech_user_fi_management.config import kc_settings
from regtech_user_fi_management.entities.listeners import setup_dao_listeners
from regtech_user_fi_management.routers import admin_router, institutions_router


log = logging.getLogger()


def run_migrations():
    file_dir = os.path.dirname(os.path.realpath(__file__))
    alembic_cfg = Config(f"{file_dir}/../../alembic.ini")
    alembic_cfg.set_main_option("script_location", f"{file_dir}/../../db_revisions")
    alembic_cfg.set_main_option("prepend_sys_path", f"{file_dir}/../../")
    command.upgrade(alembic_cfg, "head")


@asynccontextmanager
async def lifespan(app_: FastAPI):
    log.info("Starting up...")
    log.info("run alembic upgrade head...")
    run_migrations()
    await setup_dao_listeners()
    yield
    log.info("Shutting down...")


app = FastAPI(lifespan=lifespan)


app.add_exception_handler(RegTechHttpException, regtech_http_exception_handler)  # type: ignore[type-arg]  # noqa: E501
app.add_exception_handler(RequestValidationError, request_validation_error_handler)  # type: ignore[type-arg]  # noqa: E501


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exception: HTTPException) -> JSONResponse:
    log.error(exception, exc_info=True, stack_info=True)
    status = HTTPStatus(exception.status_code)
    return JSONResponse(
        status_code=exception.status_code,
        content={"error_name": status.phrase, "error_detail": jsonable_encoder(exception.detail)},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exception: Exception) -> JSONResponse:
    log.error(exception, exc_info=True, stack_info=True)
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={"error_name": "Internal Server Error", "error_detail": "server error"},
    )


oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=kc_settings.auth_url.unicode_string(), tokenUrl=kc_settings.token_url.unicode_string()
)

app.add_middleware(AuthenticationMiddleware, backend=BearerTokenAuthBackend(oauth2_scheme, OAuth2Admin(kc_settings)))
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["authorization"],
)

app.include_router(admin_router, prefix="/v1/admin")
app.include_router(institutions_router, prefix="/v1/institutions")
