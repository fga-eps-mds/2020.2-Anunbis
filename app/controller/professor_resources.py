from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas.professor_schema import ProfessorSchema
from ..services import professor_services
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError


class ProfessorDetail(Resource):
    @jwt_required()
    def get(self, name):
        professors = professor_services.get_professor_name_contains(name)
        ps = ProfessorSchema(many=True, exclude=['email', 'reg_professor'], context={'reg_student': get_jwt_identity()})
        return make_response(ps.jsonify(professors), 200)


class ProfessorList(Resource):
    def post(self):
        try:
            ps = ProfessorSchema()
            validate = ps.validate(request.json)
            professor = ps.load(request.json)
            message, status = professor_services.register_professor(professor)
            return make_response(jsonify(message), status)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)


def configure(api):
    api.add_resource(ProfessorList, "/professor")
    api.add_resource(ProfessorDetail, "/professor/<string:name>")
