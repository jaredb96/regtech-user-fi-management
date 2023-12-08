"""Update Financial Institutions Table

Revision ID: 045aa502e050
Revises: "549c612bf1c9"
Create Date: 2023-11-29 11:55:10.328766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


from db_revisions.utils import table_exists


# revision identifiers, used by Alembic.
revision: str = "045aa502e050"
down_revision: Union[str, None] = "549c612bf1c9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    if table_exists("financial_institutions"):
        op.add_column("financial_institutions", sa.Column("tax_id", sa.String(length=9), nullable=True))
        op.add_column("financial_institutions", sa.Column("rssd_id", sa.Integer(), nullable=True))
        op.create_unique_constraint("unique_association", "financial_institutions", ["tax_id", "rssd_id"])
        op.add_column(
            "financial_institutions", sa.Column("primary_federal_regulator_id", sa.String(length=4), nullable=True)
        )
        op.add_column("financial_institutions", sa.Column("hmda_institution_type_id", sa.String(), nullable=True))
        op.add_column("financial_institutions", sa.Column("sbl_institution_type_id", sa.String(), nullable=True))
        op.add_column("financial_institutions", sa.Column("hq_address_street_1", sa.String(), nullable=False))
        op.add_column("financial_institutions", sa.Column("hq_address_street_2", sa.String(), nullable=True))
        op.add_column("financial_institutions", sa.Column("hq_address_city", sa.String(), nullable=True))
        op.add_column("financial_institutions", sa.Column("hq_address_state", sa.String(length=2), nullable=True))
        op.add_column("financial_institutions", sa.Column("hq_address_zip", sa.String(length=5), nullable=False))
        op.add_column("financial_institutions", sa.Column("parent_lei", sa.String(length=20), nullable=True))
        op.add_column("financial_institutions", sa.Column("parent_legal_name", sa.String(), nullable=True))
        op.add_column("financial_institutions", sa.Column("parent_rssd_id", sa.Integer(), nullable=True))
        op.add_column("financial_institutions", sa.Column("top_holder_lei", sa.String(length=20), nullable=True))
        op.add_column("financial_institutions", sa.Column("top_holder_legal_name", sa.String(), nullable=True))
        op.add_column("financial_institutions", sa.Column("top_holder_rssd_id", sa.Integer(), nullable=True))
        op.create_index(
            op.f("ix_financial_institutions_hmda_institution_type_id"),
            "financial_institutions",
            ["hmda_institution_type_id"],
            unique=False,
        )
        op.create_index(
            op.f("ix_financial_institutions_hq_address_state"),
            "financial_institutions",
            ["hq_address_state"],
            unique=False,
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
        with op.batch_alter_table("financial_institutions") as batch_op:
            batch_op.create_foreign_key(
                "fk_federal_regulator_financial_institutions",
                "federal_regulator",
                ["primary_federal_regulator_id"],
                ["id"],
            )
            batch_op.create_foreign_key(
                "fk_address_state_financial_institutions", "address_state", ["hq_address_state"], ["code"]
            )
            batch_op.create_foreign_key(
                "fk_hmda_institution_type_financial_institutions",
                "hmda_institution_type",
                ["hmda_institution_type_id"],
                ["id"],
            )
            batch_op.create_foreign_key(
                "fk_sbl_institution_type_financial_institutions",
                "sbl_institution_type",
                ["sbl_institution_type_id"],
                ["id"],
            )


def downgrade() -> None:
    op.drop_constraint(
        constraint_name="fk_federal_regulator_financial_institutions", table_name="financial_institutions"
    )
    op.drop_constraint(constraint_name="fk_address_state_financial_institutions", table_name="financial_institutions")
    op.drop_constraint(
        constraint_name="fk_hmda_institution_type_financial_institutions", table_name="financial_institutions"
    )
    op.drop_constraint(
        constraint_name="fk_sbl_institution_type_financial_institutions", table_name="financial_institutions"
    )
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
