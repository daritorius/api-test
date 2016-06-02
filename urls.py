from src.resources import *


api.add_resource(AssetsList, '/', '/assets/')
api.add_resource(AssetsItem, '/assets/<int:asset_id>/')
api.add_resource(AssetCreditsList, '/assets/<int:asset_id>/credits/')
