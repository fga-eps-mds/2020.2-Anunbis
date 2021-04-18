from . import professor_services, student_services, discipline_services
from ..model.post import Post
from ..ext.database import db


def register_post(post):
    validate, message, status_code = __validate_post_relationship(post)
    if validate is not True:
        return message, status_code

    post_db = Post(reg_student=post.get('reg_student'), id_professor=post.get('id_professor'),
                   discipline_code=post.get('discipline_code'), content=post.get('content'), rating=post.get('rating'),
                   is_anonymous=post.get('is_anonymous'))
    db.session.add(post_db)
    db.session.commit()
    return {'message': "Post successfully added"}, 201


def __validate_post_relationship(post):
    if professor_services.get_professor_id(post.get('id_professor')) is None:
        return False, {'message': "Professor not found!"}, 404
    if student_services.get_student_reg(post.get('reg_student')) is None:
        return False, {'message': "Student not found!"}, 404
    if discipline_services.get_discipline_code(post.get('discipline_code')) is None:
        return False, {'message': "Discipline not found!"}, 404

    return True, {'message': "Ok!"}, 200
