"""Making track column unique

Revision ID: c178b9c0f058
Revises: d0dda2578926
Create Date: 2022-08-24 04:08:14.828393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c178b9c0f058'
down_revision = 'd0dda2578926'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'fieldscount', ['track'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'fieldscount', type_='unique')
    # ### end Alembic commands ###
