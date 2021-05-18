from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas import report_schema
from ..services import report_services
from flask_jwt_extended import jwt_required, current_user


class ReportList(Resource):
    @jwt_required()
    def post(self):
        user = current_user
        rs = report_schema.ReportSchema()
        report = rs.load(request.json)
        message, status_code = report_services.register_report(report, user)
        return make_response(jsonify(message), status_code)


def configure(api):
    api.add_resource(ReportList, "/report")
