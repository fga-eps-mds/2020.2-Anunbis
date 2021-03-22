from . import professor_services, student_services, discipline_services
from ..dao import post_dao
from ...ext.database import db
from ..entity.post import Post


def register_post(post):
    validate, message, status_code = __validate_post_relationship(post)
    if validate is not True:
        return message, status_code

    post_db = post_dao.Post(reg_student=post.reg_student, id_professor=post.id_professor,
                            discipline_code=post.discipline_code, content=post.content, rating=post.rating,
                            is_anonymous=post.is_anonymous)
    post_db.gen_date()
    db.session.add(post_db)
    db.session.commit()
    return {'message': "Post successfully added"}, 201


def __validate_post_relationship(post):
    if professor_services.get_professor_id(post.id_professor) is None:
        return False, {'message': "Professor not found!"}, 404
    if student_services.get_student_reg(post.reg_student) is None:
        return False, {'message': "Student not found!"}, 404
    if discipline_services.get_discipline_code(post.discipline_code) is None:
        return False, {'message': "Discipline not found!"}, 404

    return True, {'message': "Ok!"}, 200

