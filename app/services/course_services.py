from ..model import course


def get_course():
    courses_bd = course.Course.query.all()
    return courses_bd


def get_course_id(id):
    course_bd = course.Course.query.filter_by(id_course=id).first()
    return course_bd
