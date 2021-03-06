"""Books Table

Revision ID: 9af196d5fd88
Revises: 
Create Date: 2020-04-20 12:36:20.202261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9af196d5fd88'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('isbn', sa.BigInteger(), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('author', sa.PickleType(), nullable=False),
    sa.Column('category', sa.PickleType(), nullable=False),
    sa.Column('language', sa.String(length=20), nullable=False),
    sa.Column('copies', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
