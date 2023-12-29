"""create fi_to_type_mapping table

Revision ID: ada681e1877f
Revises: 383ab402c8c2
Create Date: 2023-12-29 12:33:11.031470

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from db_revisions.utils import table_exists


# revision identifiers, used by Alembic.
revision: str = "ada681e1877f"
down_revision: Union[str, None] = "383ab402c8c2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    if not table_exists("fi_to_type_mapping"):
        op.create_table(
            "fi_to_type_mapping",
            sa.Column("fi_id", sa.String(), sa.ForeignKey("financial_institutions.lei"), primary_key=True),
            sa.Column("type_id", sa.String(), sa.ForeignKey("sbl_institution_type.id"), primary_key=True),
        )


def downgrade() -> None:
    op.drop_table("fi_to_type_mapping")
