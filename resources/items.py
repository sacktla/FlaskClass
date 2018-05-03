from flask_restful import Resource
from models.item import ItemModel
class Items(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
