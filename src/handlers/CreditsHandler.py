# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from sqlalchemy.orm.exc import NoResultFound

from database.models import Credits, Thumbnail
from database.service import DatabaseService


class CreditsHandler(object):
    database_service = DatabaseService()

    @staticmethod
    def get_credits_list(sort_by=None, limit=None):
        limit = limit if limit is not None else len(Credits.query.all())
        credits_list = Credits.query.order_by(Credits.name.desc()).limit(limit).all() \
            if sort_by == 'desc' else \
            Credits.query.order_by(Credits.name.asc()).limit(limit).all()
        return credits_list

    def create_credits(self, data):
        session = self.database_service.update_db_session()
        credits_item = Credits(name=data['name'])
        session.add(credits_item)
        session.commit()
        return credits_item

    @staticmethod
    def get_credits_item(credits_id):
        credits_item = Credits.query.get(credits_id)
        if credits_item is not None:
            for asset in credits_item.assets:
                asset.credits = asset.linked_credits
                asset.thumbnails = Thumbnail.query.filter_by(asset_id=asset.id).all()
        return credits_item

    def delete_credits(self, credits_id):
        credits_item = self.get_credits_item(credits_id)
        if credits_item is not None:
            session = self.database_service.update_db_session()
            session.delete(credits_item)
            session.commit()
        return credits_item

    def update_credits(self, credits_id, data):
        session = self.database_service.update_db_session()
        try:
            credits_item = session.query(Credits).filter(Credits.id == credits_id).one()
        except NoResultFound:
            return None
        credits_item.name = data['name']
        session.commit()
        return credits_item
