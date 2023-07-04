from App import DB
from App.utils import jwt_is_blacklist, auth_required
from App.models import (
    NoteModel,
    notes_schema,
    note_schema,
)

from flask_jwt_extended import jwt_required
from flask_restful import (
    Resource,
    reqparse,
    abort,
)


class NoteResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("title", type=str)
        self.parser.add_argument("body", type=str)


    @jwt_required()
    @jwt_is_blacklist
    @auth_required
    def get(self, user_id : int):

        note : NoteModel = NoteModel.query.filter_by(user_id = user_id).all()
        if not note:
            return {}
        
        return notes_schema.dump(note)


    @jwt_required()
    @jwt_is_blacklist
    @auth_required
    def post(self, user_id : int):

        data = self.parser.parse_args()

        if not data["title"]:
            abort(401, message="Title must not be empty")

        note : NoteModel = NoteModel.query.filter_by(
            user_id = user_id, title = data["title"] ).first()
        
        if note:
            abort(404, message="Note already exists")
        
        note = NoteModel(
            user_id = user_id,
            title = data["title"],
            body = data["body"]
        )   
        DB.session.add(note)
        DB.session.commit()

        schema = note_schema.dump(note)
        return {"message" : "Successfully created", "note" : schema}, 200 
    

class UserNoteResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("title", type=str)
        self.parser.add_argument("body", type=str)


    @jwt_required()
    @jwt_is_blacklist
    @auth_required
    def get(self, note_id : int, note_title, user_id : int):
        
        note : NoteModel = NoteModel.query.filter_by(
            id = note_id, user_id = user_id, title = note_title
        ).first()

        if not note:
            abort(404, message="Note does not exists")
        
        schema = note_schema.dump(note)
        return {"note" : schema}, 200
    

    @jwt_required()
    @jwt_is_blacklist
    @auth_required
    def put(self, note_id : int, note_title, user_id : int):
        
        note : NoteModel = NoteModel.query.filter_by(
            id = note_id, user_id = user_id, title = note_title
        ).first()
        if not note:
            abort(404, message="Note does not exists")
        
        data = self.parser.parse_args()
        
        if data["title"]:
            note.title = data["title"]
        
        if data["body"]:
            note.body = data["body"]

        DB.session.commit()

        schema = note_schema.dump(note)
        return {"message" : "Update note successfully", "note" : schema}, 200


    @jwt_required()
    @jwt_is_blacklist
    @auth_required
    def delete(self, note_id : int, note_title, user_id : int):
        
        note : NoteModel = NoteModel.query.filter_by(
            id = note_id, user_id = user_id, title = note_title
        ).first()
        if not note:
            abort(404, message="Note does not exists")
        
        DB.session.delete(note)
        DB.session.commit()
        return {"message" : "Successfully deleted note"}, 200
        
