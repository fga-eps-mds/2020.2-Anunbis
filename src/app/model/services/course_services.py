from ..dao import course_dao


def get_course():
    courses = course_dao.Course.query.all()
    return courses


def get_course_id(id):
    course = course_dao.Course.query.filter_by(id_course=id).first()
    return course

