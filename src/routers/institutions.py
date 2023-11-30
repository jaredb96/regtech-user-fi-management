from fastapi import Depends, Request, HTTPException
from http import HTTPStatus
from oauth2 import oauth2_admin
from util import Router
from dependencies import check_domain, parse_leis, get_email_domain
from typing import Annotated, List, Tuple
from entities.engine import get_session
from entities.repos import institutions_repo as repo
from entities.models import (
    FinancialInstitutionDto,
    FinancialInstitutionWithDomainsDto,
    FinancialInsitutionDomainDto,
    FinancialInsitutionDomainCreate,
    FinanicialInstitutionAssociationDto,
    AuthenticatedUser,
)
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.authentication import requires


async def set_db(request: Request, session: Annotated[AsyncSession, Depends(get_session)]):
    request.state.db_session = session


router = Router(dependencies=[Depends(set_db)])


@router.get("/", response_model=List[FinancialInstitutionWithDomainsDto])
@requires("authenticated")
async def get_institutions(
    request: Request,
    leis: List[str] = Depends(parse_leis),
    domain: str = "",
    page: int = 0,
    count: int = 100,
):
    return await repo.get_institutions(request.state.db_session, leis, domain, page, count)


@router.post("/", response_model=Tuple[str, FinancialInstitutionDto], dependencies=[Depends(check_domain)])
@requires(["query-groups", "manage-users"])
async def create_institution(
    request: Request,
    fi: FinancialInstitutionDto,
):
    db_fi = await repo.upsert_institution(request.state.db_session, fi)
    kc_id = oauth2_admin.upsert_group(fi.lei, fi.name)
    return kc_id, db_fi


@router.get("/associated", response_model=List[FinanicialInstitutionAssociationDto])
@requires("authenticated")
async def get_associated_institutions(request: Request):
    user: AuthenticatedUser = request.user
    email_domain = get_email_domain(user.email)
    associated_institutions = await repo.get_institutions(request.state.db_session, user.institutions)
    return [
        FinanicialInstitutionAssociationDto(
            name=institution.name,
            lei=institution.lei,
            tax_id="123456789",
            rssd_id=1234,
            primary_federal_regulator_id="FRI1",
            hmda_institution_type_id="HIT1",
            sbl_institution_type_id="SIT1",
            hq_address_street_1="Test Address Street 1",
            hq_address_street_2="",
            hq_address_city="Test City 1",
            hq_address_state="TN",
            hq_address_zip="00000",
            parent_lei="PARENTTESTBANK123",
            parent_legal_name="PARENT TEST BANK 123",
            parent_rssd_id=12345,
            top_holder_lei="TOPHOLDERLEI123",
            top_holder_legal_name="TOP HOLDER LEI 123",
            top_holder_rssd_id=123456,
            approved=email_domain in [inst_domain.domain for inst_domain in institution.domains],
        )
        for institution in associated_institutions
    ]


@router.get("/{lei}", response_model=FinancialInstitutionWithDomainsDto)
@requires("authenticated")
async def get_institution(
    request: Request,
    lei: str,
):
    res = await repo.get_institution(request.state.db_session, lei)
    if not res:
        raise HTTPException(HTTPStatus.NOT_FOUND, f"{lei} not found.")
    return res


@router.post("/{lei}/domains/", response_model=List[FinancialInsitutionDomainDto], dependencies=[Depends(check_domain)])
@requires(["query-groups", "manage-users"])
async def add_domains(
    request: Request,
    lei: str,
    domains: List[FinancialInsitutionDomainCreate],
):
    return await repo.add_domains(request.state.db_session, lei, domains)


@router.get("/domains/allowed", response_model=bool)
async def is_domain_allowed(request: Request, domain: str):
    return await repo.is_domain_allowed(request.state.db_session, domain)
