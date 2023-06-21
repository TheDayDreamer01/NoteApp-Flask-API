from App.app import DB
from sqlalchemy.sql import func


class UserModel(DB.Model):
    __tablename__ = "users"
    
    id = DB.Column(DB.Integer, primary_key = True)

    name = DB.Column(DB.String(100), nullable=False)
    email = DB.Column(DB.String(100), nullable=False, unique=True)
    password = DB.Column(DB.String(100), nullable=False)
    date = DB.Column(
        DB.DateTime(timezone=True), 
        default=func.now()
    )
    bio = DB.Column(DB.Text, nullable=True)

    note = DB.relationship("NoteModel")


    def __repr__(self):
        return "<User %r>"%self.name