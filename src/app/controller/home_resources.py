from flask_restful import Resource


class HomeResource(Resource):
    def get(self):
        return "Hello World of my heart!"
