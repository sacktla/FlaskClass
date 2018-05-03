from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

import traceback

class Item(Resource):

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_item_by_name(name)

        if item:
            return item.json(), 200
        else:
            return {'message':'Item {} does not exist'.format(name)}, 404

    def post(self, name):
        if ItemModel.find_item_by_name(name):
            return {'message': 'An item with name {} already exists'.format(name)}, 400

        data = ItemModel.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting this item"}, 500

        return item.json(), 201

    def put(self, name):

        data = ItemModel.parser.parse_args()

        item = ItemModel.find_item_by_name(name)

        if item:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json(), 200

    def delete(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            item.delete_from_db()

        return {'message':'Item deleted'}, 200
