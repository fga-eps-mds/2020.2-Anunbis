from flask_restful import Resource
from flask import request, make_response, jsonify
from ..view import post_schema
from ..model.entity.post import Post
from ..model.services import post_services
from flask_jwt_extended import jwt_required


class PostList(Resource):
    @jwt_required()
    def post(self):
        validate = post_schema.PostSchema().validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            reg_student = request.json['reg_student']
            id_professor = request.json['id_professor']
            discipline_code = request.json['discipline_code']
            content = request.json['content']
            rating = request.json['rating']
            is_anonymous = request.json['is_anonymous']
            post = Post(reg_student, id_professor, discipline_code, content, rating, is_anonymous)

            message, status_code = post_services.register_post(post)
            return make_response(jsonify(message), status_code)


def configure(api):
    api.add_resource(PostList, "/post")