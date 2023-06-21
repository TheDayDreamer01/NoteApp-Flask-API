
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
        notes : NoteModel = NoteModel.query.filter_by(
            user_id = user.id,
            id = user_id,
            title = title
        ).first()

        return jsonify({
            "note" : notes.toObject(),
            "status" : 200
        }), 200

    return jsonify({
        "message": "User does not exist",
        "status": 404
    }), 404


@NOTE_API.route("/<int:user_id>/", methods=["POST"])
@jwt_required()
def createUserNote(user_id : int):

    return jsonify({})


@NOTE_API.route("/<int:user_id>/", methods=["PUT"])
@jwt_required()
def updateUserNote(user_id : int):
    return jsonify({})


@NOTE_API.route("/<int:user_id>/", methods=["DELETE"])
@jwt_required()
def deleteUserNote(user_id : int):
    return jsonify({})