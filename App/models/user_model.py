from marshmallow import fields
from App.app import DB, MALLOW
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


    def toObject(self) -> dict:
        return {
            "id" : self.id, 
            "name" : self.name,
            "email" : self.email,
            "bio" : self.bio
        }   
    

    def __repr__(self) -> str:
        return "<User %r>"%self.name
    

class UserSchema(MALLOW.Schema):

    class Meta:
        model : UserModel = UserModel

    name = fields.String()
    email = fields.String()
    password = fields.String()
    bio = fields.String()


user_schema = UserSchema()