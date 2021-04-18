from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas import post_schema
from ..services import post_services
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError


class PostList(Resource):
    @jwt_required()
    def post(self):
        try:
            ps = post_schema.PostSchema()
            post = ps.load(request.json)
            message, status_code = post_services.register_post(post)
            return make_response(jsonify(message), status_code)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)


def configure(api):
    api.add_resource(PostList, "/post")
