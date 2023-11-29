from typing import List, Dict, Any, Set
from pydantic import BaseModel
from starlette.authentication import BaseUser


class FinancialInsitutionDomainBase(BaseModel):
    domain: str


class FinancialInsitutionDomainCreate(FinancialInsitutionDomainBase):
    pass


class FinancialInsitutionDomainDto(FinancialInsitutionDomainBase):
    lei: str

    class Config:
        from_attributes = True


class FinancialInstitutionBase(BaseModel):
    name: str


class FinancialInstitutionDto(FinancialInstitutionBase):
    lei: str
    tax_id: str
    rssd_id: int
    primary_federal_regulator_id: str
    hmda_institution_type_id: str
    sbl_institution_type_id: str
    hq_address_street_1: str
    hq_address_street_2: str
    hq_address_city: str
    hq_address_state: str
    hq_address_zip: str
    parent_lei: str
    parent_legal_name: str
    parent_rssd_id: int
    top_holder_lei: str
    top_holder_legal_name: str
    top_holder_rssd_id: int

    class Config:
        from_attributes = True


class FinancialInstitutionWithDomainsDto(FinancialInstitutionDto):
    domains: List[FinancialInsitutionDomainDto] = []


class DeniedDomainDto(BaseModel):
    domain: str

    class Config:
        from_attributes = True


class FederalRegulatorBase(BaseModel):
    id: str


class FederalRegulatorDto(FederalRegulatorBase):
    name: str

    class Config:
        from_attributes = True


class HMDAInstitutionTypeBase(BaseModel):
    id: str


class HMDAInstitutionTypeDto(HMDAInstitutionTypeBase):
    name: str

    class Config:
        from_attributes = True


class SBLInstitutionTypeBase(BaseModel):
    id: str


class SBLInstitutionTypeDto(SBLInstitutionTypeBase):
    name: str

    class Config:
        from_attributes = True


class AddressStateBase(BaseModel):
    code: str


class AddressStateDto(AddressStateBase):
    name: str

    class Config:
        from_attributes = True


class UserProfile(BaseModel):
    first_name: str
    last_name: str
    leis: Set[str] | None = None

    def to_keycloak_user(self):
        return {"firstName": self.first_name, "lastName": self.last_name}


class FinanicialInstitutionAssociationDto(FinancialInstitutionDto):
    approved: bool


class AuthenticatedUser(BaseUser, BaseModel):
    claims: Dict[str, Any]
    name: str
    username: str
    email: str
    id: str
    institutions: List[str]

    @classmethod
    def from_claim(cls, claims: Dict[str, Any]) -> "AuthenticatedUser":
        return cls(
            claims=claims,
            name=claims.get("name", ""),
            username=claims.get("preferred_username", ""),
            email=claims.get("email", ""),
            id=claims.get("sub", ""),
            institutions=cls.parse_institutions(claims.get("institutions")),
        )

    @classmethod
    def parse_institutions(cls, institutions: List[str] | None) -> List[str]:
        """
        Parse out the list of institutions returned by Keycloak

        Args:
            institutions(List[str]): list of full institution paths provided by keycloak,
            it is possible to have nested paths, though we may not use the feature.
            e.g. ["/ROOT_INSTITUTION/CHILD_INSTITUTION/GRAND_CHILD_INSTITUTION"]

        Returns:
            List[str]: List of cleaned up institutions.
            e.g. ["GRAND_CHILD_INSTITUTION"]
        """
        if institutions:
            return [institution.split("/")[-1] for institution in institutions]
        else:
            return []

    @property
    def is_authenticated(self) -> bool:
        return True
