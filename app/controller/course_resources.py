from flask_restful import Resource
from ..model.services import course_services
from flask import request, make_response, jsonify
from ..view.course_schema import CourseSchema

class CourseList(Resource):
    def get(self):
        courses = course_services.get_course()
        cs = CourseSchema(many=True)
        return make_response(cs.jsonify(courses), 200)

