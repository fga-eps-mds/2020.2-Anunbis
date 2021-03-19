from flask_restful import Resource
from ..model.services import course_services


class TesteList(Resource):
    def get(self):
        return {"result": f" {course_services.get_course_id(10)}"}

