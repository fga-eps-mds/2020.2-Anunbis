from flasgger import Swagger


def init_app(app):
    Swagger(app)


config_specs_dict = {
    "swagger": "2.0",
    "info": {
        "title": "Anunbis back-end",
        "description": "Here is the Anunbis backend "
        "documentation API, where you can find "
        "about all of our methods and how they work. ",
        "contact": {
            "email": "anunbis.team@gmail.com",
            "url": "http://localhost:3000/",
        },
        "termsOfService": "http://localhost:3000/#contact",
        "version": "0.0.1",
    },
}
