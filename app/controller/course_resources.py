from flask_restful import Resource
from ..services import course_services
from flask import make_response
from ..schemas.course_schema import CourseSchema
from flasgger import swag_from
from . import swag_resources


class CourseList(Resource):
    @swag_from(swag_resources.course_specs_dict)
    def get(self):
        """
        This path is responsable for getting the list of courses.
        ---
        tags:
        - Course's paths

        """
        courses = course_services.get_course()
        cs = CourseSchema(many=True)
        return make_response(cs.jsonify(courses), 200)


def configure(api):
    api.add_resource(CourseList, "course")
