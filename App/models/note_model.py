from marshmallow import fields
from App.app import DB, MALLOW
from datetime import datetime


class NoteModel(DB.Model):
    __tablename__ = "notes"

    id = DB.Column(DB.Integer, primary_key = True)
    user_id = DB.Column(DB.Integer, DB.ForeignKey("users.id"))

    title = DB.Column(DB.String(100))
    body = DB.Column(DB.Text)
    date = DB.Column(
        DB.Date,
        default = datetime.now()
    )

    def __repr__(self) -> str:
        return "<Note %r>"%self.title
    
    def toObject(self) -> dict:
        return {
            "id" : self.id,
            "title" : self.title,
            "date" : self.date,
            "body" : self.body
        }

    @staticmethod
    def fromObject(data) -> "NoteModel":
        return NoteModel(
            title = data["title"],
            body = data["body"]
        )
    

class NoteSchema(MALLOW.Schema):
    class Meta:
        model : NoteModel = NoteModel

    title = fields.String()
    body = fields.String()


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)