from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
assigned = Table('assigned', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('user_id', INTEGER),
    Column('assetid', INTEGER),
    Column('reclaim', DATETIME),
)

assigned = Table('assigned', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('assetid', Integer),
    Column('reclaim_date', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['assigned'].columns['reclaim'].drop()
    post_meta.tables['assigned'].columns['reclaim_date'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['assigned'].columns['reclaim'].create()
    post_meta.tables['assigned'].columns['reclaim_date'].drop()
