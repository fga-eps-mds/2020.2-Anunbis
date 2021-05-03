from . import professor_services, student_services, discipline_services
from ..model.post import Post
from ..ext.database import db
from ..model.student import Student


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
    if discipline_services.get_discipline_code(post.get('discipline_code')) is None:
        return False, {'message': "Discipline not found!"}, 404

    return True, {'message': "Ok!"}, 200


def agree_student_post(student_db, id_post):
    post_db = Post.get(id_post=id_post)
    if post_db:
        if student_db in post_db.disagrees:
            post_db.disagrees.remove(student_db)
        if student_db in post_db.agrees:
            return unagree_post(post_db, student_db)
        else:
            return agree_post(post_db, student_db)
    else:
        return {'message': 'Post not found'}, 404


def unagree_post(post_db, student_db):
    post_db.agrees.remove(student_db)
    db.session.commit()
    return post_db, 200


def agree_post(post_db, student_db):
    post_db.agrees.append(student_db)
    db.session.commit()
    return post_db, 200


def disagree_student_post(student_db, id_post):

    post_db = Post.get(id_post=id_post)
    if post_db:
        if student_db in post_db.agrees:
            post_db.agrees.remove(student_db)
        if student_db in post_db.disagrees:
            return undisagree_post(post_db, student_db)
        else:
            return disagree_post(post_db, student_db)
    else:
        return {'message': 'post not found'}, 404


def undisagree_post(post_db, student_db):
    post_db.disagrees.remove(student_db)
    db.session.commit()
    return post_db, 200


def disagree_post(post_db, student_db):
    post_db.disagrees.append(student_db)
    db.session.commit()

    return post_db, 200 

