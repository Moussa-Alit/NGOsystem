"""adding track fields table

Revision ID: 066ddee97e38
Revises: b3b1b659acd7
Create Date: 2022-08-22 10:40:42.900724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '066ddee97e38'
down_revision = 'b3b1b659acd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('adhaactsrating')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adhaactsrating',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('starting_date_time', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('finishing_date_time', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('gps_location', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('governorate', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('its_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('p_code', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('nb_of_families', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('activity_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('if_other_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('donor', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('team_leader', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('targeted_nb_in_camp', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('distributed_items', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nb_of_itmes_to_be_distributed_in_this_act', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('exists_of_written_scheduled', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('voucher_distributed', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('beneficiaries_list_ready_used', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('protect_policies_respect_rate', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('controllcing_workplacce_rate', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('commitment_to_Covid_precautions', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('if_shortcoming_in_requirements', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('randomly_checked_item_rate', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('staff_performance', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('general_notes', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('added_by', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date_added', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('date_edited', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('existing_of_requirements', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='adhaactsrating_pkey')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('surname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('password_hash', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('date_added', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('date_edited', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    sa.UniqueConstraint('username', name='users_username_key')
    )
    # ### end Alembic commands ###
