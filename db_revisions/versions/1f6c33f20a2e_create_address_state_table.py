"""Create Address State Table

Revision ID: 1f6c33f20a2e
Revises: 20e0d51d8be9
Create Date: 2023-11-29 12:03:41.737864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1f6c33f20a2e"
down_revision: Union[str, None] = "20e0d51d8be9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "address_state",
        sa.Column("code", sa.String(length=2), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("event_time", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("code"),
        sa.UniqueConstraint("name"),
    )


def downgrade() -> None:
    op.drop_table("address_state")
