from flask_restful import Resource
from flask import request, make_response, jsonify
from ..view.student_schema import StudentSchema
from ..model.services import student_services
from ..model.entity.student import Student
from flask_jwt_extended import jwt_required, get_jwt_identity

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

    @jwt_required()
    def put(self):   
        ss = StudentSchema(only=['password'])
        validate = ss.validate(request.json)
        reg_student = int(get_jwt_identity())

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            student = Student(reg_student=reg_student,
                password=request.json['password'])
            message, status = student_services.modify_student(student)
            return make_response(jsonify(message), status)

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
