from flask_restful import Resource
from flask import request, make_response, jsonify
from ..view.student_schema import StudentSchema
from ..model.services import student_services
from ..model.entity.student import Student


class StudentList(Resource):
    def post(self):
        ss = StudentSchema()
        validate = ss.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            reg_student = request.json['reg_student']
            name = request.json['name']
            id_course = request.json['id_course']
            email = request.json['email']
            password = request.json['password']

            student = Student(reg_student=reg_student, name=name,
                              id_course=id_course,
                              email=email, password=password)
            message, status = student_services.register_student(student)
            return make_response(jsonify(message), status)


def configure(api):
    api.add_resource(StudentList, "/student")