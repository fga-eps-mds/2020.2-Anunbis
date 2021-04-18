from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas import post_schema
from ..services import post_services
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity


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

class PostAgreesList(Resource):
    @jwt_required()
    def post(self):
        reg_student = get_jwt_identity()
        ps = PostSchema()
        validate = ps.validate(request.json)
        
        if validate:
            return make_response(validate, 400)
        else:
            post, status_code = post_services.agree_student_post(reg_student, request.json['id_post'])
            if status_code == 404:
                return make_response(jsonify(post), status_code)
            else:
                return make_response(ps.jsonify(post), status_code)

class PostDisagreesList(Resource):
    @jwt_required()
    def post(self):
        reg_student = get_jwt_identity()
        ps = PostSchema()
        validate = ps.validate(request.json)
        
        if validate:
            return make_response(validate, 400)
        else:
            post, status_code = post_services.disagree_student_post(reg_student, request.json['id_post'])
            if status_code == 404:
                return make_response(jsonify(post), status_code)
            else:
                return make_response(ps.jsonify(post), status_code)

def configure(api):
    api.add_resource(PostList, "/post")
    api.add_resource(PostAgreesList, "/post/agree")
    api.add_resource(PostDisagreesList, "/post/disagree")
