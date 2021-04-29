from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas.professor_schema import ProfessorSchema
from ..services import professor_services
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError


class ProfessorDetail(Resource):
    @jwt_required()
    def get(self, name):
        validate = professor_services.validate_name(name)
        if validate:
            return make_response(jsonify(validate), 400)
        professors = professor_services.get_professor_name_contains(name)
        ps = ProfessorSchema(many=True, exclude=['email', 'reg_professor', 'posts'], context={
                             'reg_student': get_jwt_identity()})
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


class ProfessorIdDetail(Resource):
    @jwt_required()
    def get(self, id):
        try:
            ProfessorSchema(only=['id_professor']).load({'id_professor': id})
            professor = professor_services.get_professor_id(id)
            ps = ProfessorSchema(many=True, exclude=['email', 'reg_professor'], context={
                                 'reg_student': get_jwt_identity()})
            return make_response(ps.jsonify(professor), 200)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)


def configure(api):
    api.add_resource(ProfessorList, "/professor")
    api.add_resource(ProfessorDetail, "/professor/<string:name>")
    api.add_resource(ProfessorIdDetail, "/professor/<int:id>")
