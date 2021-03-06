"""new fields in user model

Revision ID: 4635350b5683
Revises: 1d936f2da914
Create Date: 2022-06-12 16:54:09.716346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4635350b5683'
down_revision = '1d936f2da914'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
