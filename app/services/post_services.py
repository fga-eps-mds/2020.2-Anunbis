from . import professor_services, discipline_services
from ..model.post import Post
from ..model.report import Report
from ..ext.database import db
from ..model.post import AgreeStudentPost, DisagreeStudentPost


def get(**kwargs):
    return Post.query.filter_by(**kwargs).first()


def delete(post_db):
    delete_feedbacks(post_db)
    delete_reports(post_db)
    db.session.delete(post_db)
    db.session.commit()


def delete_feedbacks(post_db):
    for agree in AgreeStudentPost.query.filter_by(id_post=post_db.id_post).all():
        db.session.delete(agree)
    for disagree in DisagreeStudentPost.query.filter_by(id_post=post_db.id_post).all():
        db.session.delete(disagree)
    db.session.commit()


def delete_reports(post_db):
    for report in Report.query.filter_by(id_post=post_db.id_post).all():
        db.session.delete(report)
    db.session.commit()


def register_post(post):
    validate, message, status_code = __validate_post_relationship(post)
    if validate is not True:
        return message, status_code

    post_db = Post(
        reg_student=post.get("reg_student"),
        id_professor=post.get("id_professor"),
        discipline_code=post.get("discipline_code"),
        content=post.get("content"),
        didactic=post.get("didactic"),
        metod=post.get("metod"),
        avaliations=post.get("avaliations"),
        disponibility=post.get("disponibility"),
        is_anonymous=post.get("is_anonymous"),
    )
    db.session.add(post_db)
    db.session.commit()
    return {"message": "Post successfully added"}, 201


def __validate_post_relationship(post):
    if professor_services.get(id_professor=post.get("id_professor")) is None:
        return False, {"message": "Professor not found!"}, 404
    if discipline_services.get(discipline_code=post.get("discipline_code")) is None:
        return False, {"message": "Discipline not found!"}, 404

    return True, {"message": "Ok!"}, 200


def agree_student_post(student_db, id_post):
    post_db = get(id_post=id_post)
    if post_db:
        if student_db in post_db.disagrees:
            undisagree_post(post_db, student_db)
        if student_db in post_db.agrees:
            return unagree_post(post_db, student_db)
        else:
            return agree_post(post_db, student_db)
    else:
        return {"message": "Post not found"}, 404


def unagree_post(post_db, student_db):
    post_db.agrees.remove(student_db)
    db.session.commit()
    return post_db, 200


def agree_post(post_db, student_db):
    post_db.agrees.append(student_db)
    db.session.commit()
    return post_db, 200


def disagree_student_post(student_db, id_post):
    post_db = get(id_post=id_post)
    if post_db:
        if student_db in post_db.agrees:
            unagree_post(post_db, student_db)
        if student_db in post_db.disagrees:
            return undisagree_post(post_db, student_db)
        else:
            return disagree_post(post_db, student_db)
    else:
        return {"message": "post not found"}, 404


def undisagree_post(post_db, student_db):
    post_db.disagrees.remove(student_db)
    db.session.commit()
    return post_db, 200


def disagree_post(post_db, student_db):
    post_db.disagrees.append(student_db)
    db.session.commit()

    return post_db, 200
