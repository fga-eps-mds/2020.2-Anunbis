from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas.student_schema import StudentSchema
from ..services import student_services
from flask_jwt_extended import current_user
from ..ext.auth import student_required
from flasgger import swag_from
from ..docs import student


class StudentList(Resource):
    @swag_from(student.student_post)
    def post(self):
        ss = StudentSchema()
        student = ss.load(request.json)
        message, status = student_services.register_student(student)
        return make_response(jsonify(message), status)

    @student_required()
    @swag_from(student.student_put)
    def put(self):
        ss = StudentSchema(only=["password"])
        student_db = current_user
        student_new = ss.load(request.json)
        message, status = student_services.modify_student(student_db, student_new)
        return make_response(jsonify(message), status)

    @student_required()
    @swag_from(student.student_delete)
    def delete(self):
        student = current_user
        student_services.delete(student)
        return make_response("", 204)


def configure(api):
    api.add_resource(StudentList, "student")
