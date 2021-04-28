from ..model.report import Report
from ..ext.database import db


def register_report(report):
    report_db = Report(id_report=report.get('id_report'), id_post=report.get(
        'id_post'), content=report.get('content'), reg_student=report.get('reg_student'), offensive=report.get('offensive'), prejudice=report.get('prejudice'), unrelated=report.get('unrelated'), others=report.get('others'))
    db.session.add(report_db)
    db.session.commit()

    return {'message': "Report successfully added"}, 201
