from app.models import course_model


def get_course():
    courses = course_model.Course.query.all()
    return courses

def get_course_id(id):
    course = course_model.Course.query.filter_by(id_course=id).first()
    return course

