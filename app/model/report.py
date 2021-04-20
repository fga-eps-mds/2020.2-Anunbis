from app.ext.database import db
import enum


class ReportTypes(enum.Enum):
    linguagem_ofensiva = 'L'
    incoerencia = 'I'
    grave = 'G'
    outros = 'O'


class Report(db.Model):
    __tablename__ = "report"

    id_report = db.Column(db.Integer, primary_key=True)
    id_post = db.Column(db.Integer, db.ForeignKey("post.id_post"), nullable=False)
    content = db.Column(db.String(120), nullable=False, default='')
    reg_student = db.Column(db.Integer, db.ForeignKey("student.reg_student"), nullable=False)
    report_type = db.Column(db.Enum(ReportTypes), nullable=False)
