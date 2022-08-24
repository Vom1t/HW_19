from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')

# Эндпоинт юзера
@user_ns.route('/')
class AuthView(Resource):

    def post(self):
        data = request.json
        return UserSchema().dump(user_service.create(data)), 201




