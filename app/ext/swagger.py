from flasgger import Swagger


def init_app(app):
    Swagger(app)


def config_specs_dict(ANUNBIS_FRONTEND_URI, ANUNBIS_VERSION):
    return {
        "title": "Anunbis API",
        "swagger": "2.0",
        "info": {
            "title": "Anunbis",
            "description": "Here is the Anunbis backend "
            "documentation API, where you can find "
            "about all of our methods and how they work. ",
            "contact": {
                "email": "anunbis.team@gmail.com",
                "url": ANUNBIS_FRONTEND_URI,
            },
            "termsOfService": ANUNBIS_FRONTEND_URI + "/#contact",
            "version": ANUNBIS_VERSION,
        },
        "specs": [
            {
                "endpoint": "anunbis",
                "route": "/anunbis.json",
            }
        ],
    }
