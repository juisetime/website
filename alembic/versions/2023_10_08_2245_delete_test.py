"""delete test

Revision ID: 602123c7f066
Revises: bf477a55f253
Create Date: 2023-10-08 22:45:29.501754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '602123c7f066'
down_revision = 'bf477a55f253'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_test_id', table_name='test')
    op.drop_table('test')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('test1', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('test2', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('test3', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('nametest', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='test_pkey')
    )
    op.create_index('ix_test_id', 'test', ['id'], unique=False)
    # ### end Alembic commands ###