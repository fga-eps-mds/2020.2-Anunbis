from app.ext.database import db


class Report(db.Model):
    __tablename__ = "report"

    id_report = db.Column(db.Integer, primary_key=True)
    id_post = db.Column(db.Integer, db.ForeignKey("post.id_post"), nullable=False)
    content = db.Column(db.String(120), nullable=False, default="")
    reg_student = db.Column(db.Integer, db.ForeignKey("student.reg_student"))
    id_professor = db.Column(db.Integer, db.ForeignKey("professor.id_professor"))
    offensive = db.Column(db.Boolean, nullable=False)
    prejudice = db.Column(db.Boolean, nullable=False)
    unrelated = db.Column(db.Boolean, nullable=False)
    others = db.Column(db.Boolean, nullable=False)
