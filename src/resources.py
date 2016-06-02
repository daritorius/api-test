# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with, reqparse, abort, inputs

from src.handlers.AssetsHandler import AssetsHandler
from src.args_parsers import *


app = Flask(__name__)
api = Api(app)


credits_resource_fields = {
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
        if args.get('limit') is not None:
            args['limit'] = args['limit'] if args['limit'] > 0 else None
        assets = self.assets_handler.get_assets_list(
            sort_by=args.get('sort_by'), limit=args['limit'], credits_filter=args.get('credits_filter'))
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
