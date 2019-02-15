"""init

Revision ID: d6279deb295d
Revises: 
Create Date: 2019-01-24 15:14:16.112121

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd6279deb295d'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Organisms')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Organisms',
    sa.Column('ID', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('GENUS', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('SPECIES', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('CHROMOSOME', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('PUBMEDNUM', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('NCBIASSEMBLY', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('STRAIN', mysql.VARCHAR(length=300), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
