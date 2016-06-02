from src.resources import *


api.add_resource(AssetsList, '/', '/assets/')
api.add_resource(AssetsItem, '/assets/<int:asset_id>/')
api.add_resource(AssetCreditsList, '/assets/<int:asset_id>/credits/')

api.add_resource(CreditsList, '/credits/')
api.add_resource(CreditsItem, '/credits/<int:credits_id>/')
api.add_resource(CreditsAssetsList, '/credits/<int:credits_id>/assets/')
