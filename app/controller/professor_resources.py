from flask_restful import Resource
from flask import request, make_response, jsonify
from ..view.professor_schema import ProfessorSchema
from ..model.services import professor_services
from ..model.entity.professor import Professor
from flask_jwt_extended import jwt_required

class ProfessorDetail(Resource):
    @jwt_required()
    def get(self, name):
        professors = professor_services.get_professor_name_contains(name)
        ps = ProfessorSchema(many=True, exclude=['email', 'password', 'reg_professor'])
        return make_response(ps.jsonify(professors), 200)

class ProfessorList(Resource):
    def post(self):
        ps = ProfessorSchema()
        validate = ps.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            reg_professor = request.json["reg_professor"]
            name = request.json["name"]
            email = request.json["email"]
            password = request.json["password"]

            professor = Professor(reg_professor=reg_professor, name=name,
                                    email=email, password=password)
            message, status = professor_services.register_professor(professor)
            return make_response(jsonify(message), status)
