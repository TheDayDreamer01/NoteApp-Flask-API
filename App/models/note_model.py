from App.app import DB
from sqlalchemy.sql import func


class NoteModel(DB.Model):
    __tablename__ = "notes"

    id = DB.Column(DB.Integer, primary_key = True)
    user_id = DB.Column(DB.Integer, DB.ForeignKey("users.id"))

    title = DB.Column(DB.String(100))
    note = DB.Column(DB.Text)
    date = DB.Column(
        DB.DateTime,
        default = func.now()
    )

    def __repr__(self):
        return "<Note %r>"%self.title