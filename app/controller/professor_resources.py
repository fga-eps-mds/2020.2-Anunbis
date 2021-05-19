from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas.professor_schema import ProfessorSchema
from ..services import professor_services
from flask_jwt_extended import jwt_required, get_jwt_identity, current_user
from ..ext.auth import professor_required
from flasgger import swag_from
from ..docs import professor


class ProfessorDetail(Resource):
    @swag_from(professor.professor_get_by_name)
    @jwt_required()
    def get(self, name):
        ProfessorSchema(only=["name"]).load({"name": name})
        professors = professor_services.get_name_contains(name)
        ps = ProfessorSchema(
            many=True,
            exclude=["email", "reg_professor", "posts"],
            context={"reg_student": get_jwt_identity()},
        )
        return make_response(ps.jsonify(professors), 200)


class ProfessorList(Resource):
    @swag_from(professor.professor_post)
    def post(self):
        ps = ProfessorSchema()
        professor = ps.load(request.json)
        message, status = professor_services.register_professor(professor)
        return make_response(jsonify(message), status)

    @swag_from(professor.professor_put)
    @professor_required()
    def put(self):
        ps = ProfessorSchema(only=["password"])
        professor_db = current_user
        professor_new = ps.load(request.json)
        message, status = professor_services.modify_password_professor(
            professor_db, professor_new
        )
        return make_response(jsonify(message), status)

    @swag_from(professor.professor_delete)
    @professor_required()
    def delete(self):
        professor = current_user
        message, status = professor_services.delete_professor_login(professor)
        return make_response(jsonify(message), status)


class ProfessorIdDetail(Resource):
    @swag_from(professor.professor_get_by_id)
    @jwt_required()
    def get(self, id):
        professor = professor_services.get(id_professor=id)
        ps = ProfessorSchema(
            exclude=["email", "reg_professor"],
            context={"reg_student": get_jwt_identity()},
        )
        return make_response(ps.jsonify(professor), 200)


def configure(api):
    api.add_resource(ProfessorList, "professor")
    api.add_resource(ProfessorDetail, "professor/<string:name>")
    api.add_resource(ProfessorIdDetail, "professor/<int:id>")
