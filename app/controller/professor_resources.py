from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas.professor_schema import ProfessorSchema
from ..services import professor_services
from flask_jwt_extended import jwt_required, get_jwt_identity, current_user
from ..ext.auth import professor_required


class ProfessorDetail(Resource):
    @jwt_required()
    def get(self, name):
        """
        This path is responsable for getting the professors by a part of its name.
          It needs to be given the professor's part of the name and a authorization header. 
        ---
        tags:
        - Professor's paths
        parameters:
        - in: header
          name: authorization
          type: string
          required: true
        - in: path
          name: name
          type: string
          required: true
        responses:
            200: 
                description: It will return all the professors that have part of the given name, if there's any

            400:
                description: Validation Error

        """
        ProfessorSchema(only=["name"]).load({"name": name})
        professors = professor_services.get_name_contains(name)
        ps = ProfessorSchema(
            many=True,
            exclude=["email", "reg_professor", "posts"],
            context={"reg_student": get_jwt_identity()},
        )
        return make_response(ps.jsonify(professors), 200)


class ProfessorList(Resource):
    def post(self):
        """
        This path is responsable for registering a professor
        ---
        tags:
        - Professor's paths
        parameters:
        - in: body
          name: Register a professor
          description:  It needs to be given a name, email, professor's registration,
            and a password to make this method work and register a professor in the plataform.
          schema:
                type: object
                required:
                    - name
                    - email
                    - reg_professor            
                    - password
                properties:
                    name:
                        type: string 
                    email:
                        type: string
                    reg_professor:
                        type: integer
                    password:
                        type: string
        responses:
            201: 
                description: Professor successfully registered

            400:
                description: Validation Error

            409:
                description: This professor is already registered

        """
        ps = ProfessorSchema()
        professor = ps.load(request.json)
        message, status = professor_services.register_professor(professor)
        return make_response(jsonify(message), status)

    @professor_required()
    def put(self):
        """
        This path is responsable for modfying the professor's password
        ---
        tags:
        - Professor's paths
        parameters:
        - in: header
          name: authorization
          type: string
          required: true
        - in: body
          name: Modify professor's password
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
                description: Professor password successfully changed

            400:
                description: Validation Error

            401:
                description: Missing Authorization Header

        """
        ps = ProfessorSchema(only=["password"])
        professor_db = current_user
        professor_new = ps.load(request.json)
        message, status = professor_services.modify_password_professor(
            professor_db, professor_new
        )
        return make_response(jsonify(message), status)

    @professor_required()
    def delete(self):
        """
        This path is responsable for deleting the professor's account
        It only needs to be given the authorization header 
         to validate the user and delete the professor's account.
        ---
        tags:
        - Professor's paths
        parameters:
        - in: header
          name: authorization
          type: string
          required: true
        responses:
            204: 
                description: "Nothing will be displayed"

        """
        professor = current_user
        message, status = professor_services.delete_professor_login(professor)
        return make_response(jsonify(message), status)


class ProfessorIdDetail(Resource):
    @jwt_required()
    def get(self, id):
        """
        This path is responsable for getting a professor by its id
          It needs to be given the the professor's id and a uthorization header. 
        ---
        tags:
        - Professor's paths
        parameters:
        - in: header
          name: authorization
          type: string
          required: true
        - in: path
          name: id
          type: integer
          required: true
        responses:
            200: 
                description: It will return the professor's information by the id, if there's any

        """
        professor = professor_services.get(id_professor=id)
        ps = ProfessorSchema(
            exclude=["email", "reg_professor"],
            context={"reg_student": get_jwt_identity()},
        )
        return make_response(ps.jsonify(professor), 200)


def configure(api):
    api.add_resource(ProfessorList, "professor")
    api.add_resource(ProfessorDetail, "professor/<string:name>")
    api.add_resource(ProfessorIdDetail, "professor/<int:id>")
