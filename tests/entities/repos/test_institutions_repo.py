import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from entities.models import (
    FinancialInstitutionDao,
    FinancialInstitutionDomainDao,
    FinancialInsitutionDomainCreate,
)
from entities.models import DeniedDomainDao
from entities.repos import institutions_repo as repo
from entities.models import FederalRegulatorDao
from entities.models import HMDAInstitutionTypeDao
from entities.models import SBLInstitutionTypeDao
from entities.models import AddressStateDao


class TestInstitutionsRepo:
    @pytest.fixture(scope="function", autouse=True)
    async def setup(
        self,
        transaction_session: AsyncSession,
    ):
        fi_dao_123, fi_dao_456 = FinancialInstitutionDao(
            name="Test Bank 123",
            lei="TESTBANK123",
            domains=[FinancialInstitutionDomainDao(domain="test.bank.1", lei="TESTBANK123")],
            tax_id="123456789",
            rssd_id=1234,
            primary_federal_regulator_id=FederalRegulatorDao(id="FRI1", name="Test Federal Regulator ID 1").id,
            hmda_institution_type_id=HMDAInstitutionTypeDao(id="HIT1", name="Test HMDA Instituion ID 1").id,
            sbl_institution_type_id=SBLInstitutionTypeDao(id="SIT1", name="Test SBL Instituion ID 1").id,
            hq_address_street_1="Test Address Street 1",
            hq_address_street_2="",
            hq_address_city="Test City 1",
            hq_address_state=AddressStateDao(code="TN", name="Tennessee").code,
            hq_address_zip="00000",
            parent_lei="PARENTTESTBANK123",
            parent_legal_name="PARENT TEST BANK 123",
            parent_rssd_id=12345,
            top_holder_lei="TOPHOLDERLEI123",
            top_holder_legal_name="TOP HOLDER LEI 123",
            top_holder_rssd_id=123456,
        ), FinancialInstitutionDao(
            name="Test Bank 456",
            lei="TESTBANK456",
            domains=[FinancialInstitutionDomainDao(domain="test.bank.2", lei="TESTBANK456")],
            tax_id="987654321",
            rssd_id=4321,
            primary_federal_regulator_id=FederalRegulatorDao(id="FRI2", name="Test Federal Regulator ID 2").id,
            hmda_institution_type_id=HMDAInstitutionTypeDao(id="HIT2", name="Test HMDA Instituion ID 2").id,
            sbl_institution_type_id=SBLInstitutionTypeDao(id="SIT2", name="Test SBL Instituion ID 2").id,
            hq_address_street_1="Test Address Street 2",
            hq_address_street_2="",
            hq_address_city="Test City 2",
            hq_address_state=AddressStateDao(code="TX", name="Texas").code,
            hq_address_zip="11111",
            parent_lei="PARENTTESTBANK456",
            parent_legal_name="PARENT TEST BANK 456",
            parent_rssd_id=54321,
            top_holder_lei="TOPHOLDERLEI456",
            top_holder_legal_name="TOP HOLDER LEI 456",
            top_holder_rssd_id=654321,
        )
        transaction_session.add(fi_dao_123)
        transaction_session.add(fi_dao_456)
        await transaction_session.commit()

    async def test_get_institutions(self, query_session: AsyncSession):
        res = await repo.get_institutions(query_session)
        assert len(res) == 2

    async def test_get_institutions_by_domain(self, query_session: AsyncSession):
        res = await repo.get_institutions(query_session, domain="test.bank.1")
        assert len(res) == 1

    async def test_get_institutions_by_domain_not_existing(self, query_session: AsyncSession):
        res = await repo.get_institutions(query_session, domain="testing.bank")
        assert len(res) == 0

    async def test_get_institutions_by_lei_list(self, query_session: AsyncSession):
        res = await repo.get_institutions(query_session, leis=["TESTBANK123", "TESTBANK456"])
        assert len(res) == 2

    async def test_get_institutions_by_lei_list_item_not_existing(self, query_session: AsyncSession):
        res = await repo.get_institutions(query_session, leis=["NOTTESTBANK"])
        assert len(res) == 0

    async def test_add_institution(self, transaction_session: AsyncSession):
        await repo.upsert_institution(
            transaction_session,
            FinancialInstitutionDao(
                name="New Bank 123",
                lei="NEWBANK123",
                tax_id="654321987",
                rssd_id=6543,
                primary_federal_regulator_id=FederalRegulatorDao(id="FRI3", name="Test Federal Regulator ID 3").id,
                hmda_institution_type_id=HMDAInstitutionTypeDao(id="HIT3", name="Test HMDA Instituion ID 3").id,
                sbl_institution_type_id=SBLInstitutionTypeDao(id="SIT3", name="Test SBL Instituion ID 3").id,
                hq_address_street_1="Test Address Street 3",
                hq_address_street_2="",
                hq_address_city="Test City 3",
                hq_address_state=AddressStateDao(code="CA", name="California").code,
                hq_address_zip="22222",
                parent_lei="PARENTNEWBANK123",
                parent_legal_name="PARENT NEW BANK 123",
                parent_rssd_id=76543,
                top_holder_lei="TOPHOLDERNEWBANKLEI123",
                top_holder_legal_name="TOP HOLDER NEW BANK LEI 123",
                top_holder_rssd_id=876543,
            ),
        )
        res = await repo.get_institutions(transaction_session)
        assert len(res) == 3

    async def test_update_institution(self, transaction_session: AsyncSession):
        await repo.upsert_institution(
            transaction_session,
            FinancialInstitutionDao(name="Test Bank 234", lei="TESTBANK123"),
        )
        res = await repo.get_institutions(transaction_session)
        assert len(res) == 2
        assert res[0].name == "Test Bank 234"

    async def test_add_domains(self, transaction_session: AsyncSession, query_session: AsyncSession):
        await repo.add_domains(
            transaction_session,
            "TESTBANK123",
            [FinancialInsitutionDomainCreate(domain="bank.test")],
        )
        fi = await repo.get_institution(query_session, "TESTBANK123")
        assert len(fi.domains) == 2

    async def test_domain_allowed(self, transaction_session: AsyncSession):
        denied_domain = DeniedDomainDao(domain="yahoo.com")
        transaction_session.add(denied_domain)
        await transaction_session.commit()
        assert await repo.is_domain_allowed(transaction_session, "yahoo.com") is False
        assert await repo.is_domain_allowed(transaction_session, "gmail.com") is True
