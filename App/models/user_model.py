from marshmallow import fields
from App import DB, MALLOW


class UserModel(DB.Model):
    __tablename__ = "users"
    
    id = DB.Column(DB.Integer, primary_key = True)

    username = DB.Column(DB.String(100), nullable=False)
    email = DB.Column(DB.String(100), nullable=False, unique=True)
    password = DB.Column(DB.String(100), nullable=False)
    date = DB.Column(
        DB.Date, 
        default=DB.func.current_date()
    )
    bio = DB.Column(DB.Text, nullable=True)

    note = DB.relationship("NoteModel")

    def __init__(self, username : str, email : str, password : str):
        self.username = username
        self.email = email
        self.password = password


    def __repr__(self) -> str:
        return "<User %r>"%self.username


    def toObject(self) -> dict:
        return {
            "id" : self.id, 
            "username" : self.username,
            "email" : self.email,
            "bio" : self.bio
        }   
    
    @staticmethod
    def fromObject(data) -> "UserModel":
        return UserModel(
            username = data["username"],   
            email = data["email"],
            password = data["password"],
            bio = data["bio"]
        )


class UserSchema(MALLOW.Schema):

    class Meta:
        model : UserModel = UserModel
        fields : tuple = ("id", "username", "email", "bio")

    username = fields.String()
    email = fields.String()
    password = fields.String()
    bio = fields.String()


user_schema = UserSchema()