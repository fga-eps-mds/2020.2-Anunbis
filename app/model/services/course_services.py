from ..dao import course_dao
from ..entity.course import Course


def get_course():
    courses_bd = course_dao.Course.query.all()
    courses = [Course(course_bd=course_bd) for course_bd in courses_bd]
    return courses


def get_course_id(id):
    course_bd = course_dao.Course.query.filter_by(id_course=id).first()
    return Course(course_bd=course_bd)
