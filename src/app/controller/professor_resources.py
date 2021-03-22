from flask_restful import Resource
from ..model.services import professor_services
from flask import make_response, jsonify
from ..view.professor_schema import ProfessorSchema


class ProfessorDetail(Resource):
    def get(self, name):
        professors = professor_services.get_professor_name_contains(name)
        ps = ProfessorSchema(many=True, exclude=['email', 'password', 'reg_professor'])
        return make_response(ps.jsonify(professors), 200)

