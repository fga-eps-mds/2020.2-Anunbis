from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas.student_schema import StudentSchema
from ..services import student_services
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError


class StudentList(Resource):
    def post(self):
        try:
            ss = StudentSchema()
            student = ss.load(request.json)
            message, status = student_services.register_student(student)
            return make_response(jsonify(message), status)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

    @jwt_required()
    def put(self):   
        try:
            ss = StudentSchema(only=['password'])
            reg_student = int(get_jwt_identity())
            student = ss.load(request.json)
            student['reg_student'] = reg_student
            message, status = student_services.modify_student(student)
            return make_response(jsonify(message), status)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)


class StudentDetail(Resource):
    @jwt_required()
    def delete(self, reg_student):
        if int(get_jwt_identity()) != reg_student:
            return make_response(jsonify({'message': "Authorization Header Invalid"}), 401)

        message, status_code = student_services.delete_student_by_reg(reg_student)
        return make_response(jsonify(message), status_code)


def configure(api):
    api.add_resource(StudentList, "/student")
    api.add_resource(StudentDetail, "/student/<int:reg_student>")
