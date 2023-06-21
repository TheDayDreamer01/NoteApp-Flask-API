from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from App.config import Config


JWT : JWTManager = JWTManager()
DB : SQLAlchemy = SQLAlchemy()
BCRYPT : Bcrypt = Bcrypt()


def create_note_app(config_class : Config = Config) -> Flask:

    note_app : Flask = Flask(__name__)
    CORS(note_app)

    note_app.config.from_object(config_class)
    JWT.init_app(note_app)
    DB.init_app(note_app)
    BCRYPT.init_app(note_app)


    from App.apis.auth import AUTH_API
    from App.apis.note import NOTE_API
    from App.apis.user import USER_API

    
    note_app.register_blueprint(AUTH_API, url_prefix="/api/auth")
    note_app.register_blueprint(NOTE_API, url_prefix="/api/note")
    note_app.register_blueprint(USER_API, url_prefix="/api/user")


    from App.models import (
        UserModel,
        NoteModel
    )

    with note_app.app_context():
        DB.create_all()

    return note_app