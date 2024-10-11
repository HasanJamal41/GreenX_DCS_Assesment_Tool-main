"""question_answer

Revision ID: 362df1345cbe
Revises: 
Create Date: 2024-08-20 11:57:22.848152

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision = '362df1345cbe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_name'), 'company', ['name'], unique=False)
    op.create_table('framework_types',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('sustainability_types',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('token_blacklist',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('access_token', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_token_blacklist_access_token'), 'token_blacklist', ['access_token'], unique=True)
    op.create_table('top_of_mind_types',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_top_of_mind_types_name'), 'top_of_mind_types', ['name'], unique=True)
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('user_token', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_user_token'), 'user', ['user_token'], unique=True)
    op.create_table('domain_types',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('framework_subtypes',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('framework_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['framework_type_id'], ['framework_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_framework_subtypes_framework_type_id'), 'framework_subtypes', ['framework_type_id'], unique=False)
    op.create_table('new_password_code',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_index(op.f('ix_new_password_code_user_id'), 'new_password_code', ['user_id'], unique=False)
    op.create_table('other_measures',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('sustainability_types_id', sa.Integer(), nullable=False),
    sa.Column('other_measure', sqlmodel.sql.sqltypes.AutoString(length=2000), nullable=False),
    sa.ForeignKeyConstraint(['sustainability_types_id'], ['sustainability_types.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_other_measures_sustainability_types_id'), 'other_measures', ['sustainability_types_id'], unique=False)
    op.create_index(op.f('ix_other_measures_user_id'), 'other_measures', ['user_id'], unique=False)
    op.create_table('otp_password',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('code', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('expiration_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_email'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_index(op.f('ix_otp_password_user_email'), 'otp_password', ['user_email'], unique=True)
    op.create_table('sustainability_measures',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('typically_selected', sa.Boolean(), nullable=True),
    sa.Column('sustainability_types_id', sa.Integer(), nullable=True),
    sa.Column('top_of_mind_types_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sustainability_types_id'], ['sustainability_types.id'], ),
    sa.ForeignKeyConstraint(['top_of_mind_types_id'], ['top_of_mind_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sustainability_measures_sustainability_types_id'), 'sustainability_measures', ['sustainability_types_id'], unique=False)
    op.create_index(op.f('ix_sustainability_measures_top_of_mind_types_id'), 'sustainability_measures', ['top_of_mind_types_id'], unique=False)
    op.create_table('questions',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('is_single_choice', sa.Boolean(), nullable=True),
    sa.Column('framework_subtypes_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['framework_subtypes_id'], ['framework_subtypes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_questions_framework_subtypes_id'), 'questions', ['framework_subtypes_id'], unique=False)
    op.create_table('roles',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('domain_type_id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['domain_type_id'], ['domain_types.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_domain_type_id'), 'roles', ['domain_type_id'], unique=False)
    op.create_table('user_selected_measures',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sustainability_measures_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sustainability_measures_id'], ['sustainability_measures.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_selected_measures_sustainability_measures_id'), 'user_selected_measures', ['sustainability_measures_id'], unique=False)
    op.create_index(op.f('ix_user_selected_measures_user_id'), 'user_selected_measures', ['user_id'], unique=False)
    op.create_table('answers',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('answer', sa.Text(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('questions_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['questions_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_answers_questions_id'), 'answers', ['questions_id'], unique=False)
    op.create_table('comment',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_comment'), 'comment', ['comment'], unique=False)
    op.create_table('top_of_mind_roles',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('top_of_mind_types_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['top_of_mind_types_id'], ['top_of_mind_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_top_of_mind_roles_role_id'), 'top_of_mind_roles', ['role_id'], unique=False)
    op.create_index(op.f('ix_top_of_mind_roles_top_of_mind_types_id'), 'top_of_mind_roles', ['top_of_mind_types_id'], unique=False)
    op.create_table('user_profiles',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('domain_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['domain_id'], ['domain_types.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('user_selected_answers',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answer_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['answer_id'], ['answers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_selected_answers_answer_id'), 'user_selected_answers', ['answer_id'], unique=False)
    op.create_index(op.f('ix_user_selected_answers_user_id'), 'user_selected_answers', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_selected_answers_user_id'), table_name='user_selected_answers')
    op.drop_index(op.f('ix_user_selected_answers_answer_id'), table_name='user_selected_answers')
    op.drop_table('user_selected_answers')
    op.drop_table('user_profiles')
    op.drop_index(op.f('ix_top_of_mind_roles_top_of_mind_types_id'), table_name='top_of_mind_roles')
    op.drop_index(op.f('ix_top_of_mind_roles_role_id'), table_name='top_of_mind_roles')
    op.drop_table('top_of_mind_roles')
    op.drop_index(op.f('ix_comment_comment'), table_name='comment')
    op.drop_table('comment')
    op.drop_index(op.f('ix_answers_questions_id'), table_name='answers')
    op.drop_table('answers')
    op.drop_index(op.f('ix_user_selected_measures_user_id'), table_name='user_selected_measures')
    op.drop_index(op.f('ix_user_selected_measures_sustainability_measures_id'), table_name='user_selected_measures')
    op.drop_table('user_selected_measures')
    op.drop_index(op.f('ix_roles_domain_type_id'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_questions_framework_subtypes_id'), table_name='questions')
    op.drop_table('questions')
    op.drop_index(op.f('ix_sustainability_measures_top_of_mind_types_id'), table_name='sustainability_measures')
    op.drop_index(op.f('ix_sustainability_measures_sustainability_types_id'), table_name='sustainability_measures')
    op.drop_table('sustainability_measures')
    op.drop_index(op.f('ix_otp_password_user_email'), table_name='otp_password')
    op.drop_table('otp_password')
    op.drop_index(op.f('ix_other_measures_user_id'), table_name='other_measures')
    op.drop_index(op.f('ix_other_measures_sustainability_types_id'), table_name='other_measures')
    op.drop_table('other_measures')
    op.drop_index(op.f('ix_new_password_code_user_id'), table_name='new_password_code')
    op.drop_table('new_password_code')
    op.drop_index(op.f('ix_framework_subtypes_framework_type_id'), table_name='framework_subtypes')
    op.drop_table('framework_subtypes')
    op.drop_table('domain_types')
    op.drop_index(op.f('ix_user_user_token'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_top_of_mind_types_name'), table_name='top_of_mind_types')
    op.drop_table('top_of_mind_types')
    op.drop_index(op.f('ix_token_blacklist_access_token'), table_name='token_blacklist')
    op.drop_table('token_blacklist')
    op.drop_table('sustainability_types')
    op.drop_table('framework_types')
    op.drop_index(op.f('ix_company_name'), table_name='company')
    op.drop_table('company')
    # ### end Alembic commands ###
