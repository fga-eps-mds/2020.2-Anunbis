from app.models import course_model


def get_course():
    courses = course_model.Course.query.all()
    return courses
