from marshmallow import fields
from App.app import DB, MALLOW
from sqlalchemy.sql import func

class NoteModel(DB.Model):
    __tablename__ = "notes"

    id = DB.Column(DB.Integer, primary_key = True)
    user_id = DB.Column(DB.Integer, DB.ForeignKey("users.id"))

    title = DB.Column(DB.String(100))
    body = DB.Column(DB.Text)
    date = DB.Column(
        DB.DateTime(timezone=True),
        default = func.now()
    )

    def __init__(self, user_id : int, title : str, body : str):
        self.user_id = user_id
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return "<Note %r>"%self.title
    
    def toObject(self) -> dict:
        return {
            "id" : self.id,
            "title" : self.title,
            "date" : self.date,
            "body" : self.body
        }


class NoteSchema(MALLOW.Schema):
    class Meta:
        model : NoteModel = NoteModel
        fields : tuple = ("id", "title", "body", "date") 

    title = fields.String()
    body = fields.String()


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)