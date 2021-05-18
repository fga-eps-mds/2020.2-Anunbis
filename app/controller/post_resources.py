from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas import post_schema
from ..services import post_services
from flask_jwt_extended import current_user, jwt_required
from ..ext.auth import student_required
from marshmallow import ValidationError
from flasgger import swag_from
from ..docs import post


class PostList(Resource):
    @swag_from(post.post_list_get)
    @jwt_required()
    def get(self):
        user = current_user
        if not user.is_professor():
            ps = post_schema.PostSchema(many=True, context={"reg_student": user.reg})
        else:
            ps = post_schema.PostSchema(many=True)
        return make_response(ps.jsonify(user.posts), 200)

    @swag_from(post.post_list_post)
    @student_required()
    def post(self):
        ps = post_schema.PostSchema(exclude=["id_post"])
        post = ps.load(request.json)
        if post.get("reg_student") != current_user.reg_student:
            raise ValidationError(
                {"reg_student": "Your reg_student is different to" " post.reg_student"}
            )
        message, status_code = post_services.register_post(post)
        return make_response(jsonify(message), status_code)


class PostAgreesList(Resource):
    @swag_from(post.post_list_postAgree)
    @student_required()
    def post(self):
        student = current_user
        ps = post_schema.PostSchema(only=["id_post"])
        id = ps.load(request.json).get("id_post")
        post, status_code = post_services.agree_student_post(student, id)
        if status_code == 200:
            ps = post_schema.PostSchema(context={"reg_student": student.reg_student})
            return make_response(ps.jsonify(post), status_code)
        else:
            return make_response(jsonify(post), status_code)


class PostDisagreesList(Resource):
    @swag_from(post.post_list_postDisagree)
    @student_required()
    def post(self):
        student = current_user
        ps = post_schema.PostSchema(only=["id_post"])
        id = ps.load(request.json).get("id_post")
        post, status_code = post_services.disagree_student_post(student, id)
        if status_code == 404:
            return make_response(jsonify(post), status_code)
        else:
            ps = post_schema.PostSchema(context={"reg_student": student.reg_student})
            return make_response(ps.jsonify(post), status_code)


def configure(api):
    api.add_resource(PostList, "post")
    api.add_resource(PostAgreesList, "post/agree")
    api.add_resource(PostDisagreesList, "post/disagree")
