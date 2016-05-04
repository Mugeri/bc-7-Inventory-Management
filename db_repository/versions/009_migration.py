from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
assets = Table('assets', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('assetname', VARCHAR(length=64)),
    Column('assetdescription', VARCHAR(length=500)),
    Column('serialnumber', VARCHAR(length=50)),
    Column('andelaserial', VARCHAR(length=50)),
    Column('datebought', DATETIME),
    Column('available', BOOLEAN),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['assets'].columns['datebought'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['assets'].columns['datebought'].create()
