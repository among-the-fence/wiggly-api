"""new start

Revision ID: e7466844cbcd
Revises: 
Create Date: 2021-12-21 15:46:34.100082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7466844cbcd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hero',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('localized_name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hero_id'), 'hero', ['id'], unique=False)
    op.create_table('match',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('winner', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_match_id'), 'match', ['id'], unique=False)
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_team_id'), 'team', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('did', sa.BigInteger(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('confidence', sa.Float(), nullable=True),
    sa.Column('shortname', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_confidence'), 'user', ['confidence'], unique=False)
    op.create_index(op.f('ix_user_did'), 'user', ['did'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_rating'), 'user', ['rating'], unique=False)
    op.create_table('pick',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('hero_id', sa.Integer(), nullable=False),
    sa.Column('match_id', sa.Integer(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hero_id'], ['hero.id'], ),
    sa.ForeignKeyConstraint(['match_id'], ['match.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pick_id'), 'pick', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pick_id'), table_name='pick')
    op.drop_table('pick')
    op.drop_index(op.f('ix_user_rating'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_did'), table_name='user')
    op.drop_index(op.f('ix_user_confidence'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_team_id'), table_name='team')
    op.drop_table('team')
    op.drop_index(op.f('ix_match_id'), table_name='match')
    op.drop_table('match')
    op.drop_index(op.f('ix_hero_id'), table_name='hero')
    op.drop_table('hero')
    # ### end Alembic commands ###