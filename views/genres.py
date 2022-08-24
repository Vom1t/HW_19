from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from service.decorators import auth_required, admin_required

genre_ns = Namespace('genres')

# Эндпоинт для получения всех жанров и добавления с разными правами
@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        data = request.json
        return GenreSchema().dump(genre_service.create(data)), 201

# Эндпоинт для получения одного жанра и добавления, удаления с разными правами
@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, rid):
        data = request.json
        if not data.get('id') or (data.get('id') != rid):
            data['id'] = rid

        return GenreSchema().dump(genre_service.update(data)), 200

    @admin_required
    def delete(self, rid):
        return genre_service.delete(rid), 200
