from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
assets = Table('assets', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('assetname', String(length=64)),
    Column('assetdescription', String(length=500)),
    Column('serialnumber', String(length=50)),
    Column('andelaserial', String(length=50)),
    Column('datebought', DateTime),
)

assigned = Table('assigned', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('assetid', Integer),
    Column('reclaim', DateTime),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('password', String(length=120)),
    Column('level', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['assets'].create()
    post_meta.tables['assigned'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['assets'].drop()
    post_meta.tables['assigned'].drop()
    post_meta.tables['user'].drop()
