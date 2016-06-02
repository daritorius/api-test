# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with, reqparse, abort, inputs

from src.handlers.AssetsHandler import AssetsHandler
from src.args_parsers import *
from src.handlers.CreditsHandler import CreditsHandler

app = Flask(__name__)
api = Api(app)


# credits_resource_fields = {
#     'name': fields.String,
# }


credits_resource_fields = {
    'id': fields.String,
    'name': fields.String,
}


thumbnails_resource_fields = {
    'image_url': fields.String,
}


assets_resource_fields = {
    'id': fields.String,
    'title': fields.String,
    'description': fields.String,
    'created_at': fields.DateTime(dt_format='rfc822'),
    'credits': fields.Nested(credits_resource_fields),
    'thumbnails': fields.Nested(thumbnails_resource_fields),
}


class AssetsList(Resource):
    assets_handler = AssetsHandler()

    @marshal_with(assets_resource_fields)
    def get(self):
        args = assets_list_parser.parse_args(strict=True)
        assets = self.assets_handler.get_assets_list(
            sort_by=args.get('sort_by'), limit=args.get('limit'), credits_filter=args.get('credits_filter'))
        return assets, 200

    @marshal_with(assets_resource_fields)
    def post(self):
        args = assets_create_parser.parse_args(strict=True)
        asset = self.assets_handler.create_asset(args)
        return asset, 200


class AssetsItem(Resource):
    assets_handler = AssetsHandler()

    @marshal_with(assets_resource_fields)
    def get(self, asset_id):
        assets_item_parser.parse_args(strict=True)
        asset = self.assets_handler.get_asset(asset_id)
        if asset is None:
            abort(500, message="No asset with id {}".format(asset_id))
        return asset, 200

    @marshal_with(assets_resource_fields)
    def put(self, asset_id):
        args = assets_item_update_parser.parse_args(strict=True)
        asset = self.assets_handler.update_asset(asset_id, args)
        if asset is None:
            abort(500, message="No asset with id {}".format(asset_id))
        return asset, 200

    def delete(self, asset_id):
        assets_item_parser.parse_args(strict=True)
        asset = self.assets_handler.delete_asset(asset_id)
        if asset is None:
            abort(500, message="No asset with id {}".format(asset_id))
        return {}, 201


class AssetCreditsList(Resource):
    assets_handler = AssetsHandler()

    @marshal_with(credits_resource_fields)
    def get(self, asset_id):
        assets_item_parser.parse_args(strict=True)
        asset_credits = self.assets_handler.get_asset_credits(asset_id)
        if asset_credits is None:
            abort(500, message="No asset with id {}".format(asset_id))
        return asset_credits, 200


class CreditsList(Resource):
    credits_handler = CreditsHandler()

    @marshal_with(credits_resource_fields)
    def get(self):
        args = credits_list_parser.parse_args(strict=True)
        credits_list = self.credits_handler.get_credits_list(sort_by=args.get('sort_by'), limit=args.get('limit'))
        return credits_list, 200

    @marshal_with(credits_resource_fields)
    def post(self):
        args = credits_create_parser.parse_args(strict=True)
        credits_item = self.credits_handler.create_credits(args)
        return credits_item, 200


class CreditsItem(Resource):
    credits_handler = CreditsHandler()

    @marshal_with(credits_resource_fields)
    def get(self, credits_id):
        credits_item_parser.parse_args(strict=True)
        credits_item = self.credits_handler.get_credits_item(credits_id)
        if credits_item is None:
            abort(500, message="No credits with id {}".format(credits_id))
        return credits_item, 200

    @marshal_with(credits_resource_fields)
    def put(self, credits_id):
        args = credits_item_update_parser.parse_args(strict=True)
        credits_item = self.credits_handler.update_credits(credits_id, args)
        if credits_item is None:
            abort(500, message="No credits with id {}".format(credits_item))
        return credits_item, 200

    def delete(self, credits_id):
        credits_item_parser.parse_args(strict=True)
        credits_item = self.credits_handler.delete_credits(credits_id)
        if credits_item is None:
            abort(500, message="No credits with id {}".format(credits_item))
        return {}, 201


class CreditsAssetsList(Resource):
    credits_handler = CreditsHandler()

    @marshal_with(assets_resource_fields)
    def get(self, credits_id):
        credits_item_parser.parse_args(strict=True)
        credits_item = self.credits_handler.get_credits_item(credits_id)
        if credits_item is None:
            abort(500, message="No credits with id {}".format(credits_id))
        return credits_item.assets, 200
