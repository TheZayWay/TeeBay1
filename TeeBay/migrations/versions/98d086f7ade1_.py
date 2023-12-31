"""empty message

Revision ID: 98d086f7ade1
Revises: 
Create Date: 2023-07-12 12:35:06.594293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98d086f7ade1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.Column('teeshirts_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teeshirts_id'], ['teeshirts.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teeshirts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=False),
    sa.Column('brand', sa.String(length=50), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('carts_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['carts_id'], ['carts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('brands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('teeshirts_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teeshirts_id'], ['teeshirts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('carts_teeshirts',
    sa.Column('carts_id', sa.Integer(), nullable=False),
    sa.Column('teeshirts_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['carts_id'], ['carts.id'], ),
    sa.ForeignKeyConstraint(['teeshirts_id'], ['teeshirts.id'], ),
    sa.PrimaryKeyConstraint('carts_id', 'teeshirts_id')
    )
    op.create_table('listings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teeshirts_id', sa.Integer(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teeshirts_id'], ['teeshirts.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('listings_users',
    sa.Column('listings_id', sa.Integer(), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['listings_id'], ['listings.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('listings_id', 'users_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('listings_users')
    op.drop_table('listings')
    op.drop_table('carts_teeshirts')
    op.drop_table('brands')
    op.drop_table('users')
    op.drop_table('teeshirts')
    op.drop_table('carts')
    # ### end Alembic commands ###
