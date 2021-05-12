from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas.student_schema import StudentSchema
from ..services import student_services
from flask_jwt_extended import current_user
from ..ext.auth import student_required


class StudentList(Resource):
    def post(self):
        """
        This path is responsable for registering a student
        ---
        tags:
        - Student's paths
        parameters:
        - in: body
          name: Register a studant
          description:  It needs to be given a name, email, student's registration,
           course's identification and a password to make this method work and register a
           student in the plataform.
          schema:
                type: object
                required:
                    - name
                    - email
                    - reg_student
                    - id_course
                    - password
                properties:
                    name:
                        type: string
                    email:
                        type: string
                    reg_student:
                        type: integer
                    id_course:
                        type: integer
                    password:
                        type: string
        responses:
            201:
                description: Student successfully registered

            400:
                description: Validation Error

            404:
                description: Course not found

            409:
                description: Student already registered

        """
        ss = StudentSchema()
        student = ss.load(request.json)
        message, status = student_services.register_student(student)
        return make_response(jsonify(message), status)

    @student_required()
    def put(self):
        """
        This path is responsable for modfying the student's password
        ---
        tags:
        - Student's paths
        parameters:
        - in: header
          name: authorization
          type: string
          required: true
        - in: body
          name: Modify student's password
          description:  It needs to be given the authorization header
           to validate the user, and the new password to be able to modify the old one.
          schema:
                type: object
                required:
                    - password
                properties:
                    password:
                        type: string
        responses:
            200:
                description: Student successfully changed

            400:
                description: Validation Error

            401:
                description: Missing Authorization Header

        """
        ss = StudentSchema(only=["password"])
        student_db = current_user
        student_new = ss.load(request.json)
        message, status = student_services.modify_student(
            student_db, student_new)
        return make_response(jsonify(message), status)

    @student_required()
    def delete(self):
        """
        This path is responsable for deleting the student's account
        It only needs to be given the authorization header
         to validate the user and delete the student's account.
        ---
        tags:
        - Student's paths
        parameters:
        - in: header
          name: authorization
          type: string
          required: true
        responses:
            204:
                description: "Nothing will be displayed"

        """
        student = current_user
        student_services.delete(student)
        return make_response("", 204)


def configure(api):
    api.add_resource(StudentList, "student")
