# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from database.settings import db_session, engine
from sqlalchemy.orm import sessionmaker


class DatabaseService(object):

    def update_db_session(self):
        db_session.remove()
        Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        session = Session()
        return session
