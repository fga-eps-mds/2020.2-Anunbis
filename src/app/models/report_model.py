from ..ext.database import db
import enum


class ReportTypes(enum.Enum):
    linguagem_ofensiva = 'L'
    incoerencia = 'I'
    grave = 'G'
    outros = 'O'


class Report(db.Model):
    __tablename__ = "REPORT"

    id_report = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_post = db.Column(db.Integer, db.ForeignKey("POST.id_post"), nullable=False)
    content = db.Column(db.String(120), nullable=False, default='')
    reg_student = db.Column(db.Integer, db.ForeignKey("STUDENT.reg_student"), nullable=False)
    report_type = db.Column(db.Enum(ReportTypes), nullable=False)
