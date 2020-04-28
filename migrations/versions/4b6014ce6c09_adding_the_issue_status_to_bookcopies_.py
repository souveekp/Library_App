"""Adding the issue_status to bookcopies table

Revision ID: 4b6014ce6c09
Revises: 56f9c9656a11
Create Date: 2020-04-27 19:29:03.376908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b6014ce6c09'
down_revision = '56f9c9656a11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book_copies', sa.Column('issue_status', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book_copies', 'issue_status')
    # ### end Alembic commands ###
