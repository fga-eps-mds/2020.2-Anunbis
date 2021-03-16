from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas.student_schema import StudentSchema
from ..services import student_services


class StudentList(Resource):
    def post(self):
        ss = StudentSchema()
        validate = ss.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            message, status = student_services.register_student(request.json)
            return make_response(message, status)



