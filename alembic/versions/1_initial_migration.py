"""initial migration

Revision ID: 1
Revises: 
Create Date: 2024-08-30 18:36:43.735985

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'noises',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('max_volume', sa.Float(), nullable=True),
        sa.Column('step', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'videos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('video_id', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('noises')
    op.drop_table('videos')
