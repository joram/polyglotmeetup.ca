"""create notification request table

Revision ID: 803b9c0bed50
Revises: 7a21e17d4a91
Create Date: 2022-06-21 15:37:00.592009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '803b9c0bed50'
down_revision = '7a21e17d4a91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notification_requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notification_requests')
    # ### end Alembic commands ###