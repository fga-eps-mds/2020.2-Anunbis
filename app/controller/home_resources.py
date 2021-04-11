from flask_restful import Resource


class HomeList(Resource):
    def get(self):
        return "Hello World of my heart!"


def configure(api):
    api.add_resource(HomeList, "/")