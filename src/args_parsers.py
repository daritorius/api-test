# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from flask_restful import reqparse, inputs


assets_list_parser = reqparse.RequestParser()
assets_list_parser.add_argument('sort_by', choices=('asc', 'desc'), type=str, help='Sort assets: asc or desc',
                                trim=True)
assets_list_parser.add_argument('limit', type=int, help='Limit amount of results')
assets_list_parser.add_argument('credits_filter', type=str, help="Filter assets by credit's title", trim=True)


assets_create_parser = reqparse.RequestParser()
assets_create_parser.add_argument('title', required=True, type=str, help='Title for asset')
assets_create_parser.add_argument('description', type=str, help='Description for asset')
assets_create_parser.add_argument('created_at', type=inputs.datetime_from_rfc822, help='Date of creation for asset')
assets_create_parser.add_argument('credits_names', type=str, action='append', help='Credits name for asset')
assets_create_parser.add_argument('thumbnails', type=str, action='append', help='Thumbnail url for asset')


assets_item_parser = reqparse.RequestParser()


assets_item_update_parser = reqparse.RequestParser()
assets_item_update_parser.add_argument('title', type=str, help="Asset's title")
assets_item_update_parser.add_argument('description', type=str, help="Asset's description")
assets_item_update_parser.add_argument('created_at', type=inputs.datetime_from_rfc822,
                                       help='Date of creation for asset')
