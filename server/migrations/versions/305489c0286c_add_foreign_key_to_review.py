"""add foreign key to Review

Revision ID: 305489c0286c
Revises: 14773b011ca9
Create Date: 2025-01-15 09:13:12.104569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '305489c0286c'
down_revision = '14773b011ca9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    # ### end Alembic commands ###
