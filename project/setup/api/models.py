from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссеры', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Алис Ли'),
})

movie: Model = api.model('Фильмы', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Матрица'),
    'description': fields.String(required=True, max_length=300, example='Обо всем'),
    'trailer': fields.String(required=True, max_length=100, example='Ссылка'),
    'year': fields.Integer(required=True, max_length=100, example='2021'),
    'rating': fields.Float(required=True, max_length=100, example='1,4'),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director)
})

user: Model = api.model('Пользователи', {
    'id': fields.Integer(required=True, example=1, autoincrement=True),
    'email': fields.String(required=True, max_length=100, example='test@test.com'),
    'password': fields.String(required=True, max_length=300, example='qwerty_1'),
    'name': fields.String(required=True, max_length=100, example='John'),
    'surname': fields.String(required=True, max_length=100, example='Snow'),
    'favorite_genre': fields.Nested(genre)
})

