from flask_restful import Resource, fields, marshal_with, reqparse, Api
from flask import jsonify
from app.api import bp
from app.extensions import api as api_ext

api = Api(bp)


class HelloWorld(Resource):
    def get(self, id="world"):
        return {"hello": id}

    def post(self):
        return ""


userSchema = {
    "id": fields.Integer(default=0),
    "username": fields.String,
    "is_active": fields.Boolean(default=True),
}

def stringValidate(value):
    if value and type(value) == "string":
        return value
    else:
        raise ValueError()

userUpdateParser = reqparse.RequestParser()
userUpdateParser.add_argument(
    "username", required=True, type=stringValidate, help="This field is req!"
)


class User(Resource):
    @marshal_with(userSchema)
    def get(self, id):
        return {"username": "USER", "is_active": "fsdf"}

    def put(self, id):
        return {"PUT": id}

    def delete(self, id):
        return {"DELETE": id}

    @marshal_with(userSchema)
    def post(self, id):
        args = userUpdateParser.parse_args()
        
        return {**args}


class UserList(Resource):
    def get(self):
        return [{}]


api.add_resource(HelloWorld, "/", "/hello-world/<string:id>")
api.add_resource(User, "/user/<int:id>")
api.add_resource(UserList, "/user")
