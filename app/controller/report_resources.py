from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas import report_schema
from ..services import report_services
from flask_jwt_extended import jwt_required, current_user


class ReportList(Resource):
    @jwt_required()
    def post(self):
        """
        This path is responsable for registering a report
        ---
        tags:
        - Report's paths
        parameters:
        - in: header
          name: authorization
          type: string
          required: true
        - in: body
          name: Register a report
          description:  It needs to be given the authorization header
            to validate the user, have a written content, a id_post,
             and be a true or false for the variables offensive, prejudice, unrelated and others,
             and then be able to register a report in the plataform.
          schema:
                type: object
                required:
                    - id_post
                    - offensive
                    - prejudice
                    - unrelated
                    - others
                    - content
                properties:
                    id_post:
                        type: integer
                    offensive:
                        type: boolean
                    prejudice:
                        type: boolean
                    unrelated:
                        type: boolean
                    others:
                        type: boolean
                    content:
                        type: string
        responses:
            201:
                description: Report successfully added

            400:
                description: Validation Error

            404:
                description: Course not found

        """
        user = current_user
        rs = report_schema.ReportSchema()
        report = rs.load(request.json)
        message, status_code = report_services.register_report(report, user)
        return make_response(jsonify(message), status_code)



def configure(api):
    api.add_resource(ReportList, "report")
