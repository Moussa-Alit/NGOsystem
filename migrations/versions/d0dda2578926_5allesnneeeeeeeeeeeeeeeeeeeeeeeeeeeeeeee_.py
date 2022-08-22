"""5allesnneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

Revision ID: d0dda2578926
Revises: 1dd092af5b43
Create Date: 2022-08-22 14:35:10.162746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0dda2578926'
down_revision = '1dd092af5b43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fieldscount',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('track', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fieldscount')
    # ### end Alembic commands ###
