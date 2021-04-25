from flask_jwt_extended import JWTManager

jwt = JWTManager()


def init_app(app):
    jwt.init_app(app)


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.reg
