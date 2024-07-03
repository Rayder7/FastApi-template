"""create access_token

Revision ID: c3aae01eb039
Revises: 584f552cd436
Create Date: 2024-07-03 19:38:05.407233

"""
from typing import Sequence, Union

import fastapi_users_db_sqlalchemy
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3aae01eb039'
down_revision: Union[str, None] = '584f552cd436'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'accesstokens',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('token', sa.String(length=43), nullable=False),
        sa.Column('created_at', fastapi_users_db_sqlalchemy.generics.TIMESTAMPAware(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
            name=op.f('fk_accesstokens_user_id_users'),
            ondelete='cascade',
        ),
        sa.PrimaryKeyConstraint('token', name=op.f('pk_accesstokens'))
    )
    op.create_index(op.f('ix_accesstokens_created_at'), 'accesstokens', ['created_at'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_accesstokens_created_at'), table_name='accesstokens')
    op.drop_table('accesstokens')
