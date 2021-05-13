from flask_restful import Resource
from ..services import course_services
from flask import make_response
from ..schemas.course_schema import CourseSchema


class CourseList(Resource):
    def get(self):
        """
        This path is responsable for getting the list of courses.
        ---
        tags:
        - Course's paths
        responses:
            200:
                description: It will return all the courses, if there's any

        """
        courses = course_services.get_course()
        cs = CourseSchema(many=True)
        return make_response(cs.jsonify(courses), 200)


def configure(api):
    api.add_resource(CourseList, "course")
