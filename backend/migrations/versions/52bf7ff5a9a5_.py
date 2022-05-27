"""empty message

Revision ID: 52bf7ff5a9a5
Revises: 
Create Date: 2022-05-27 11:53:33.883928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52bf7ff5a9a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('survey',
    sa.Column('survey_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('survey_name', sa.String(length=80), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('category', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('survey_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('role', sa.Enum('USER', 'ADMIN', name='rolesenum'), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('channel',
    sa.Column('channel_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('channel_name', sa.String(length=80), nullable=False),
    sa.Column('admin_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['admin_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('channel_id')
    )
    op.create_table('survey_parties',
    sa.Column('survey_party_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('survey_id', sa.Integer(), nullable=False),
    sa.Column('party_name', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['survey_id'], ['survey.survey_id'], ),
    sa.PrimaryKeyConstraint('survey_party_id')
    )
    op.create_table('survey_responses',
    sa.Column('response_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('survey_id', sa.Integer(), nullable=False),
    sa.Column('responsed_user_id', sa.Integer(), nullable=False),
    sa.Column('responsed_to', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['responsed_user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['survey_id'], ['survey.survey_id'], ),
    sa.PrimaryKeyConstraint('response_id')
    )
    op.create_table('channel_subscriptions',
    sa.Column('subscription_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('subscribed_channel_id', sa.Integer(), nullable=False),
    sa.Column('subscriber_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subscribed_channel_id'], ['channel.channel_id'], ),
    sa.ForeignKeyConstraint(['subscriber_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('subscription_id')
    )
    op.create_table('news',
    sa.Column('news_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('headline', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=80), nullable=False),
    sa.Column('category', sa.String(length=80), nullable=False),
    sa.Column('hashtag', sa.String(length=80), nullable=True),
    sa.Column('posted_by', sa.Integer(), nullable=False),
    sa.Column('channel_id', sa.Integer(), nullable=True),
    sa.Column('posted_date', sa.DateTime(), nullable=False),
    sa.Column('edited_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['channel_id'], ['channel.channel_id'], ),
    sa.ForeignKeyConstraint(['posted_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('news_id')
    )
    op.create_table('images',
    sa.Column('image_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('news_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['news_id'], ['news.news_id'], ),
    sa.PrimaryKeyConstraint('image_id')
    )
    op.create_table('user_news',
    sa.Column('user_news_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('news_id', sa.Integer(), nullable=False),
    sa.Column('is_saved', sa.Boolean(), nullable=False),
    sa.Column('is_liked', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['news_id'], ['news.news_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_news_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_news')
    op.drop_table('images')
    op.drop_table('news')
    op.drop_table('channel_subscriptions')
    op.drop_table('survey_responses')
    op.drop_table('survey_parties')
    op.drop_table('channel')
    op.drop_table('user')
    op.drop_table('survey')
    # ### end Alembic commands ###
