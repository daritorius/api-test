import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_folder = os.path.abspath(os.path.dirname(__file__))
database_name = 'api.db'

engine = create_engine('sqlite:///%s/%s' % (database_folder, database_name), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import database.models
    Base.metadata.create_all(bind=engine)
