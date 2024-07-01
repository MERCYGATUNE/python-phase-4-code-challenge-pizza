"""message

Revision ID: 245d5c20e935
Revises: aec3cd342203
Create Date: 2024-07-01 23:46:59.932973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '245d5c20e935'
down_revision = 'aec3cd342203'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant_pizzas', sa.Column('restaurant_id', sa.Integer(), nullable=True))
    op.add_column('restaurant_pizzas', sa.Column('pizza_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_restaurant_pizzas_restaurant_id_restaurants'), 'restaurant_pizzas', 'restaurants', ['restaurant_id'], ['id'])
    op.create_foreign_key(op.f('fk_restaurant_pizzas_pizza_id_pizzas'), 'restaurant_pizzas', 'pizzas', ['pizza_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_restaurant_pizzas_pizza_id_pizzas'), 'restaurant_pizzas', type_='foreignkey')
    op.drop_constraint(op.f('fk_restaurant_pizzas_restaurant_id_restaurants'), 'restaurant_pizzas', type_='foreignkey')
    op.drop_column('restaurant_pizzas', 'pizza_id')
    op.drop_column('restaurant_pizzas', 'restaurant_id')
    # ### end Alembic commands ###
