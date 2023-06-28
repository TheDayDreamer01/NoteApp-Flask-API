from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS


BCRYPT : Bcrypt = Bcrypt()
DB : SQLAlchemy = SQLAlchemy()
JWT : JWTManager = JWTManager()
MALLOW : Marshmallow = Marshmallow()


def create_note_app(environment) -> Flask:

    note_app : Flask = Flask(__name__)
    note_app.config.from_object(environment)
    
    API = Api(note_app)
    JWT.init_app(note_app)
    DB.init_app(note_app)
    BCRYPT.init_app(note_app)
    MALLOW.init_app(note_app)
    CORS(note_app)


    from App.apis.auth import (
        SignUpResource,
        SignInResource,
        SignOutResource
    )   
    from App.apis.note import NoteResource
    from App.apis.user import UserResource


    API.add_resource(SignUpResource, "/api/auth/signup")
    API.add_resource(SignInResource, "/api/auth/signin")
    API.add_resource(SignOutResource, "/api/auth/signout")

    API.add_resource(NoteResource, "/api/note/<int:user_id>")

    API.add_resource(UserResource, "/api/user/<int:user_id>")
    

    with note_app.app_context():
        DB.create_all()

    return note_app