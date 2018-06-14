import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        required=True,
        help = "This field cannot be left blank"
    )

    parser.add_argument(
        'password',
        required=True,
        help = "This field cannot be left blank"
    )

    def post(self):

        data = UserRegister.parser.parse_args()

        if not UserModel.find_by_username(data['username']):
            user = UserModel(data['username'], data['password'])
            user.save_to_db()
            return {"message": "User {} created successfully.".format(data['username'])}, 201

        return {"message": "Username {} already existed.".format(data['username'])}, 409
