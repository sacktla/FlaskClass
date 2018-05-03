from flask_restful import Resource
from models.store import StoreModel

class Stores(Resource):
    def get(self):
        return {'stores' : [store.json() for store in StoreModel.query.all()]}
