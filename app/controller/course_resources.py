from flask_restful import Resource
from ..services import course_services
from flask import make_response
from ..schemas.course_schema import CourseSchema


class CourseList(Resource):
    def get(self):
        courses = course_services.get_course()
        cs = CourseSchema(many=True)
        return make_response(cs.jsonify(courses), 200)


def configure(api):
    api.add_resource(CourseList, "/course")
