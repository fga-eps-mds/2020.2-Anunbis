from flask_marshmallow import Marshmallow

ma = Marshmallow()

def configure(app):
    ma.init_app(app)