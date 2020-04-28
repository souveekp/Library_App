"""Adding the BooksIssued table and making the necessary changes in other tables to support it

Revision ID: 3fcc11622b0b
Revises: 41f0c7ae44d3
Create Date: 2020-04-27 19:03:48.999017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fcc11622b0b'
down_revision = '41f0c7ae44d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books_issued',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('issuer_id', sa.Integer(), nullable=True),
    sa.Column('issuer_name', sa.String(length=50), nullable=True),
    sa.Column('issued_book_id', sa.Integer(), nullable=True),
    sa.Column('issue_date', sa.Date(), nullable=True),
    sa.Column('expected_return_date', sa.Date(), nullable=True),
    sa.Column('actual_return_date', sa.Date(), nullable=True),
    sa.Column('fine', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['issued_book_id'], ['book_copies.book_copy_id'], ),
    sa.ForeignKeyConstraint(['issuer_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['issuer_name'], ['user.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books_issued')
    # ### end Alembic commands ###
