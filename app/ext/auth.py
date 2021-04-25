from flask_jwt_extended import JWTManager
from ..model import user


jwt = JWTManager()


def init_app(app):
    jwt.init_app(app)


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.reg


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return user.get(reg=identity)
