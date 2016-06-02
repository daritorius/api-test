# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from sqlalchemy.orm.exc import NoResultFound

from database.models import Asset, Thumbnail, Credits
from database.service import DatabaseService


class AssetsHandler(object):
    database_service = DatabaseService()

    def create_asset(self, data):
        session = self.database_service.update_db_session()
        if data.get('created_at') is not None:
            data['created_at'] = data['created_at'].replace(tzinfo=None)
        asset = Asset(title=data['title'], description=data.get('description'), created_at=data.get('created_at'))
        session.add(asset)
        if data.get('credits_names') is not None:
            for name in data['credits_names']:
                credits_obj = Credits(name=name)
                session.add(credits_obj)
                asset.linked_credits.append(credits_obj)
        session.commit()
        asset.thumbnails = []
        if data.get('thumbnails') is not None:
            for image_url in data['thumbnails']:
                thumbnail = Thumbnail(image_url=image_url, asset_id=asset.id)
                session.add(thumbnail)
                asset.thumbnails.append(thumbnail)
        session.commit()
        asset.credits = asset.linked_credits
        return asset

    @staticmethod
    def get_assets_list(sort_by=None, limit=None, credits_filter=None):
        limit = limit if limit is not None else len(Asset.query.all())
        if credits_filter is not None and len(credits_filter.strip()):
            assets = Asset.query\
                .join(Asset.linked_credits, aliased=True)\
                .filter(Credits.name.contains(credits_filter))\
                .order_by(Asset.title.desc()).limit(limit).all() \
                if sort_by == 'desc' else \
                Asset.query\
                .join(Asset.linked_credits, aliased=True)\
                .filter(Credits.name.contains(credits_filter))\
                .order_by(Asset.title.asc()).limit(limit).all()
        else:
            assets = Asset.query.order_by(Asset.title.desc()).limit(limit).all() \
                if sort_by == 'desc' else \
                Asset.query.order_by(Asset.title.asc()).limit(limit).all()
        for asset in assets:
            asset.credits = asset.linked_credits
            asset.thumbnails = Thumbnail.query.filter_by(asset_id=asset.id).all()
        return assets

    @staticmethod
    def get_asset(asset_id):
        asset = Asset.query.get(asset_id)
        if asset is not None:
            asset.credits = asset.linked_credits
            asset.thumbnails = Thumbnail.query.filter_by(asset_id=asset_id).all()
        return asset

    def update_asset(self, asset_id, data):
        session = self.database_service.update_db_session()
        try:
            asset = session.query(Asset).filter(Asset.id == asset_id).one()
        except NoResultFound:
            return None
        if data.get('title') is not None:
            asset.title = data['title']
        if data.get('description') is not None:
            asset.description = data['description']
        if data.get('created_at') is not None:
            asset.created_at = data['created_at'].replace(tzinfo=None)
        session.commit()
        asset.credits = asset.linked_credits
        asset.thumbnails = Thumbnail.query.filter_by(asset_id=asset_id).all()
        return asset

    def delete_asset(self, asset_id):
        asset = self.get_asset(asset_id)
        if asset is not None:
            session = self.database_service.update_db_session()
            session.delete(asset)
            session.commit()
        return asset

    def get_asset_credits(self, asset_id):
        asset = self.get_asset(asset_id)
        if asset is not None:
            return asset.credits
        return None
