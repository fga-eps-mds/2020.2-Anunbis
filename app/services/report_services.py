from ..model.report import Report
from ..ext.database import db
from . import student_services, post_services


def register_report(report):
    validate, message, status_code = __validate_report_relationship(report)
    if validate is not True:
        return message, status_code

    report_db = Report(id_report=report.get('id_report'), id_post=report.get(
        'id_post'), content=report.get('content'), reg_student=report.get('reg_student'), offensive=report.get('offensive'), prejudice=report.get('prejudice'), unrelated=report.get('unrelated'), others=report.get('others'))
    db.session.add(report_db)
    db.session.commit()

    return {'message': "Report successfully added"}, 201

def __validate_report_relationship(report):
    if student_services.get_student_reg(report.get('reg_student')) is None:
        return False, {'message': "Student not found!"}, 404

    return True, {'message': "Ok!"}, 200
