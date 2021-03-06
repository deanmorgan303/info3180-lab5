"""empty message

Revision ID: 63ae609af2c7
Revises: 55a26061f1b1
Create Date: 2019-02-27 16:41:40.546291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63ae609af2c7'
down_revision = '55a26061f1b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
