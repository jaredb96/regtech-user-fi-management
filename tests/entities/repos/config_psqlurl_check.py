    @field_validator("inst_conn", mode='before')
    @classmethod
    def encode_db_password(cls, postgres_dsn, info: FieldValidationInfo) -> Any:
        log = logging.getLogger()
        pwd = re.search('.*:.*:(.*)@', postgres_dsn)
        if pwd:
            pwd_str = pwd.group(1)
            qout = parse.quote(pwd_str, safe='')
            return postgres_dsn.replace(pwd_str, qout)
        else:
            log.error(f"Postgres DSN did not contain a properly formatted URL: {postgres_dsn}")