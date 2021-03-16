from flask_restful import Resource
from app.blueprints.services import course_services
from flask import request, make_response, jsonify
from app.blueprints.schemas import course_schema

class CourseList(Resource):
    def get(self):
        courses = course_services.get_course()
        cs = course_schema.CourseSchema(many=True)
        return make_response(cs.jsonify(courses), 200)

