#You don't have to use jsonify anymore
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

#Security
from security import authenticate, identity

#Resources
from resources.user_register import UserRegister
from resources.item import Item
from resources.items import Items
from resources.store import Store
from resources.stores import Stores

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

#This is the code to create the tables
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Stores, '/stores')
api.add_resource(Store, '/store/<string:name>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    app.run(port=5000, debug=True)
