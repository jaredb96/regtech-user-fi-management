"""Update Financial Institutions Table

Revision ID: 045aa502e050
Revises: 20e0d51d8be9
Create Date: 2023-11-29 11:55:10.328766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "045aa502e050"
down_revision: Union[str, None] = "20e0d51d8be9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on = ["1f6c33f20a2e", "8b1ba6a3275b", "56ef0b5cd2d4", "549c612bf1c9"]


def upgrade() -> None:
    op.add_column("financial_institutions", sa.Column("tax_id", sa.String(length=9), nullable=False))
    op.add_column("financial_institutions", sa.Column("rssd_id", sa.Integer(), nullable=False))
    op.add_column(
        "financial_institutions", sa.Column("primary_federal_regulator_id", sa.String(length=4), nullable=False)
    )
    op.add_column("financial_institutions", sa.Column("hmda_institution_type_id", sa.String(), nullable=False))
    op.add_column("financial_institutions", sa.Column("sbl_institution_type_id", sa.String(), nullable=False))
    op.add_column("financial_institutions", sa.Column("hq_address_street_1", sa.String(), nullable=False))
    op.add_column("financial_institutions", sa.Column("hq_address_street_2", sa.String(), nullable=False))
    op.add_column("financial_institutions", sa.Column("hq_address_city", sa.String(), nullable=False))
    op.add_column("financial_institutions", sa.Column("hq_address_state", sa.String(length=2), nullable=False))
    op.add_column("financial_institutions", sa.Column("hq_address_zip", sa.String(length=5), nullable=False))
    op.add_column("financial_institutions", sa.Column("parent_lei", sa.String(length=20), nullable=False))
    op.add_column("financial_institutions", sa.Column("parent_legal_name", sa.String(), nullable=False))
    op.add_column("financial_institutions", sa.Column("parent_rssd_id", sa.Integer(), nullable=False))
    op.add_column("financial_institutions", sa.Column("top_holder_lei", sa.String(length=20), nullable=False))
    op.add_column("financial_institutions", sa.Column("top_holder_legal_name", sa.String(), nullable=False))
    op.add_column("financial_institutions", sa.Column("top_holder_rssd_id", sa.Integer(), nullable=False))
    op.create_index(
        op.f("ix_financial_institutions_hmda_institution_type_id"),
        "financial_institutions",
        ["hmda_institution_type_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_financial_institutions_hq_address_state"), "financial_institutions", ["hq_address_state"], unique=False
    )
    op.create_index(
        op.f("ix_financial_institutions_primary_federal_regulator_id"),
        "financial_institutions",
        ["primary_federal_regulator_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_financial_institutions_sbl_institution_type_id"),
        "financial_institutions",
        ["sbl_institution_type_id"],
        unique=False,
    )
    op.create_unique_constraint(None, "financial_institutions", ["rssd_id"])
    op.create_unique_constraint(None, "financial_institutions", ["tax_id"])
    op.create_foreign_key(None, "financial_institutions", "federal_regulator", ["primary_federal_regulator_id"], ["id"])
    op.create_foreign_key(None, "financial_institutions", "address_state", ["hq_address_state"], ["code"])
    op.create_foreign_key(None, "financial_institutions", "hmda_institution_type", ["hmda_institution_type_id"], ["id"])
    op.create_foreign_key(None, "financial_institutions", "sbl_institution_type", ["sbl_institution_type_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_column("financial_institutions", "top_holder_rssd_id")
    op.drop_column("financial_institutions", "top_holder_legal_name")
    op.drop_column("financial_institutions", "top_holder_lei")
    op.drop_column("financial_institutions", "parent_rssd_id")
    op.drop_column("financial_institutions", "parent_legal_name")
    op.drop_column("financial_institutions", "parent_lei")
    op.drop_column("financial_institutions", "hq_address_zip")
    op.drop_column("financial_institutions", "hq_address_state")
    op.drop_column("financial_institutions", "hq_address_city")
    op.drop_column("financial_institutions", "hq_address_street_2")
    op.drop_column("financial_institutions", "hq_address_street_1")
    op.drop_column("financial_institutions", "sbl_institution_type_id")
    op.drop_column("financial_institutions", "hmda_institution_type_id")
    op.drop_column("financial_institutions", "primary_federal_regulator_id")
    op.drop_column("financial_institutions", "rssd_id")
    op.drop_column("financial_institutions", "tax_id")
    # ### end Alembic commands ###
