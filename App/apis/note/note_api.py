from App.app import DB
from App.models import (
    NoteModel, 
    UserModel, 
    notes_schema,
    note_schema
)

from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restful import (
    Resource,
    reqparse,
)


class NoteResource(Resource):
    @jwt_required
    def get(self, user_id : int):
        user : UserModel = UserModel.query.filter_by(id=user_id).first()
        if not user:
            return jsonify({"User does not exists"}), 404
        
        note : NoteModel = NoteModel.query.filter_by(user_id = user_id).all()
        return notes_schema.dump(note)
    

class UserNoteResource(Resource):
    def __init__(self):

        self.parser = reqparse.RequestParser()
        self.parser.add_argument("title", type=str)
        self.parser.add_argument("body", type=str)


    @jwt_required
    def get(self, note_id : int, note_title, user_id : int):
        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            return jsonify({"message" : "User does not exists"}), 404
        
        note : NoteModel = NoteModel.query.filter_by(
            id = note_id, user_id = user_id, title = note_title
        ).first()

        if not note:
            return jsonify({"message" : "Note does not exists"}), 404
        
        return note_schema.dump(note), 200
        


    @jwt_required
    def post(self, note_id : int, note_title, user_id : int):
        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            return jsonify({"message" : "User does not exists"}), 404
        
        note : NoteModel = NoteModel.query.filter_by(
            id = note_id, user_id = user_id, title = note_title
        ).first()
        if note:
            return jsonify({"message" : "Note already exists"}), 404
        
        note = NoteModel.fromObject(self.parser.parse_args())
        DB.session.add(note)
        DB.session.commit()
    
        return jsonify({"message" : "Created successfully"}), 200 
    

    @jwt_required
    def put(self, note_id : int, note_title, user_id : int):
        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            return jsonify({"message" : "User does not exists"}), 404
        
        note : NoteModel = NoteModel.query.filter_by(
            id = note_id, user_id = user_id, title = note_title
        ).first()
        if not note:
            return jsonify({"message" : "Note does not exists"}), 404
        
        data = self.parser.parse_args()
        
        if data["title"]:
            note.title = data["title"]
        
        if data["body"]:
            note.body = data["body"]

        DB.session.commit()
        return jsonify({"message" : "Update note successfully"}), 200


    @jwt_required
    def delete(self, note_id : int, note_title, user_id : int):
        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            return jsonify({"message" : "User does not exists"}), 404
        
        note : NoteModel = NoteModel.query.filter_by(
            id = note_id, user_id = user_id, title = note_title
        ).first()
        if not note:
            return jsonify({"message" : "Note does not exists"}), 404
        
        DB.session.delete(note)
        DB.session.commit()
        return jsonify({"message" : "Successfully deleted note"}), 200
        
