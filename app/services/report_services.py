from ..model.report import Report
from ..ext.database import db
from . import post_services


def register_report(report, user):
    message, status_code = validate_post(report.get("id_post"))

    if status_code == 404:
        return message, status_code

    report_db = Report(
        id_post=report.get("id_post"),
        content=report.get("content"),
        offensive=report.get("offensive"),
        prejudice=report.get("prejudice"),
        unrelated=report.get("unrelated"),
        others=report.get("others"),
    )
    if user.is_professor():
        report_db.id_professor = user.id_professor
    else:
        report_db.reg_student = user.reg_student
    db.session.add(report_db)
    db.session.commit()

    return {"message": "Report successfully added"}, 201


def validate_post(id_post):
    if post_services.get(id_post=id_post) is None:
        return {"message": "Post not found!"}, 404
    return None, None
