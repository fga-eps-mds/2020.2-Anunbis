from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt
from ..model import user
from functools import wraps


jwt = JWTManager()


def init_app(app):
    jwt.init_app(app)


def student_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_student"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Students only!"), 403

        return decorator

    return wrapper

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.reg


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return user.get(reg=identity)
