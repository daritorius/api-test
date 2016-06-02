from database.settings import Base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship


credits_assets = Table(
    'credits_assets', Base.metadata,
    Column('assets_id', Integer, ForeignKey('assets.id')),
    Column('credits_id', Integer, ForeignKey('credits.id'))
)


class Credits(Base):
    __tablename__ = 'credits'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Credits: %s>' % self.name


class Asset(Base):
    __tablename__ = 'assets'

    id = Column(Integer, primary_key=True)
    title = Column(String(254))
    description = Column(String(254), nullable=True)
    created_at = Column(DateTime)
    linked_credits = relationship("Credits", secondary=credits_assets, backref='assets')

    def __init__(self, title, description, created_at):
        self.title = title
        self.description = description
        self.created_at = created_at

    def __repr__(self):
        return '<Asset: %s>' % self.title


class Thumbnail(Base):
    __tablename__ = 'thumbnails'

    id = Column(Integer, primary_key=True)
    image_url = Column(String(254))
    asset_id = Column(Integer, ForeignKey('assets.id'))

    def __init__(self, image_url, asset_id):
        self.asset_id = asset_id
        self.image_url = image_url

    def __repr__(self):
        return '<Thumbnail: %s>' % self.asset_id


