from App.app import DB
from App.models import (
    NoteModel, 
    UserModel, 
    notes_schema,
    note_schema
)

from flask_jwt_extended import jwt_required
from flask_restful import (
    Resource,
    reqparse,
)


class NoteResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("title", type=str)
        self.parser.add_argument("body", type=str)


    @jwt_required()
    def get(self, user_id : int):
        user : UserModel = UserModel.query.filter_by(id=user_id).first()
        if not user:
            return {"User does not exists"}, 404
        
        note : NoteModel = NoteModel.query.filter_by(user_id = user_id).all()
        if not note:
            return {}
        
        return notes_schema.dump(note)


    @jwt_required()
    def post(self, user_id : int):
        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            return {"message" : "User does not exists"}, 404
        
        data = self.parser.parse_args()

        note : NoteModel = NoteModel.query.filter_by(
            user_id = user_id, title = data["title"] ).first()
        
        if note:
            return {"message" : "Note already exists"}, 404
        
        note = NoteModel(
            user_id = user_id,
            title = data["title"],
            body = data["body"]
        )   
        DB.session.add(note)
        DB.session.commit()
    
        return {"note" : note.toObject()}, 200 
    

class UserNoteResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("title", type=str)
        self.parser.add_argument("body", type=str)


    @jwt_required()
    def get(self, note_id : int, note_title, user_id : int):
        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            return {"message" : "User does not exists"}, 404
        
        note : NoteModel = NoteModel.query.filter_by(
            id = note_id, user_id = user_id, title = note_title
        ).first()

        if not note:
            return {"message" : "Note does not exists"}, 404
        
        schema = note_schema.dump(note)
        return {"note" : schema}, 200
    

    @jwt_required()
    def put(self, note_id : int, note_title, user_id : int):
        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            return {"message" : "User does not exists"}, 404
        
        note : NoteModel = NoteModel.query.filter_by(
            id = note_id, user_id = user_id, title = note_title
        ).first()
        if not note:
            return {"message" : "Note does not exists"}, 404
        
        data = self.parser.parse_args()
        
        if data["title"]:
            note.title = data["title"]
        
        if data["body"]:
            note.body = data["body"]

        DB.session.commit()
        return {"message" : "Update note successfully"}, 200


    @jwt_required()
    def delete(self, note_id : int, note_title, user_id : int):
        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            return {"message" : "User does not exists"}, 404
        
        note : NoteModel = NoteModel.query.filter_by(
            id = note_id, user_id = user_id, title = note_title
        ).first()
        if not note:
            return {"message" : "Note does not exists"}, 404
        
        DB.session.delete(note)
        DB.session.commit()
        return {"message" : "Successfully deleted note"}, 200
        
