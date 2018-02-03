"""initial db

Revision ID: ad03991ab4e9
Revises: 
Create Date: 2018-02-03 01:25:12.712512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad03991ab4e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('tag', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('page_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['page_id'], ['page.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu')
    op.drop_table('page')
    # ### end Alembic commands ###
