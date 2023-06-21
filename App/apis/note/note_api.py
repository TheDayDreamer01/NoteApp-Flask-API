from App.app import DB
from App.models import NoteModel, UserModel
from flask import (
    Blueprint,
    request,
    jsonify
)

from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)


NOTE_API : Blueprint = Blueprint("NOTE_API", __name__)


@NOTE_API.route("/", methods=["GET"])
@jwt_required()
def getNote():
    access_token = get_jwt_identity()
    user : UserModel = UserModel.query.filter_by(email=access_token).first()

    if user:
        notes : NoteModel = NoteModel.query.filter_by(user_id=user.id).all()
        note_list : list = []

        for note in notes:
            note_list.append(note.toObject())

        return jsonify({
            "notes": note_list,
            "status" : 200
        }), 200

    return jsonify({
        "message": "User does not exist",
        "status": 404
    }), 404


@NOTE_API.route("/<int:user_id>/<title>/", methods=["GET"])
@jwt_required()
def getUserNote(user_id : int, title : str):
    access_token = get_jwt_identity()
    user : UserModel = UserModel.query.filter_by(email=access_token).first()

    if user:
        note : NoteModel = NoteModel.query.filter_by(
            user_id = user.id,
            id = user_id,
            title = title
        ).first()

        return jsonify({
            "note" : note.toObject(),
            "status" : 200
        }), 200

    return jsonify({
        "message": "User does not exist",
        "status": 404
    }), 404


@NOTE_API.route("/", methods=["POST"])
@jwt_required()
def createUserNote():

    access_token = get_jwt_identity()
    user : UserModel = UserModel.query.filter_by(email = access_token).first()

    if user:
        title = request.form["title"]
        body = request.form["body"]

        note : NoteModel = NoteModel.query.filter_by(title=title).first()
        if not note:

            note = NoteModel(
                title = title,
                body = body
            )

            DB.session.add(note)
            DB.session.commit()

            return jsonify({
                "message" : "Successfully Created Note",
                "status" : 200
            }), 200
        
        else:
            return jsonify({
                "message" : "Title already Exists",
                "status" : 400
            }), 400
        

    return jsonify({
        "message": "User does not exist",
        "status": 404
    }), 404


@NOTE_API.route("/<int:user_id>/<title>/", methods=["PUT"])
@jwt_required()
def updateUserNote(user_id : int, title : str):
    
    access_token = get_jwt_identity()
    user : UserModel = UserModel.query.filter_by(email=access_token).first()

    if user:
        note : NoteModel = NoteModel.query.filter_by(
            id = user_id,
            user_id = user.id,
            title = title
        )
        note.title = request.get_json()["title"]
        note.body = request.get_json()["body"]
        DB.session.commit()

        return jsonify({
            "message" : "Successfully Updated Note",
            "status" : 200
        }), 200


    return jsonify({
        "message": "User does not exist",
        "status": 404
    }), 404


@NOTE_API.route("/<int:user_id>/<title>/", methods=["DELETE"])
@jwt_required()
def deleteUserNote(user_id : int, title : str):

    access_token = get_jwt_identity()
    user : UserModel = UserModel.query.filter_by(email=access_token).first()

    if user:
        note : NoteModel = NoteModel.query.filter_by(
            user_id = user.id,
            id = user_id,
            title = title
        ).first()

        DB.session.delete(note)
        DB.session.commit()

        return jsonify({
            "message" : "Successfully Deleted Note",
            "status" : 200
        }), 200

    return jsonify({
        "message": "User does not exist",
        "status": 404
    }), 404