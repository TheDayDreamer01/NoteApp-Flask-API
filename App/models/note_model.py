from App.app import DB
from sqlalchemy.sql import func
from flask import jsonify


class NoteModel(DB.Model):
    __tablename__ = "notes"

    id = DB.Column(DB.Integer, primary_key = True)
    user_id = DB.Column(DB.Integer, DB.ForeignKey("users.id"))

    title = DB.Column(DB.String(100))
    body = DB.Column(DB.Text)
    date = DB.Column(
        DB.DateTime,
        default = func.now()
    )

    def __repr__(self):
        return "<Note %r>"%self.title
    
        
    def toObject(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "date" : self.date,
            "body" : self.body
        }