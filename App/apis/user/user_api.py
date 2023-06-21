from App.models import UserModel
from App.app import DB, BCRYPT
from flask import (
    Blueprint,
    request,
    jsonify
)
from flask_jwt_extended import (
    jwt_required,
    unset_jwt_cookies,
    unset_access_cookies,
    get_jwt_identity
)


USER_API : Blueprint = Blueprint("USER_API", __name__)


@USER_API.route("/<int:user_id>/", methods=["GET"])
@jwt_required()
def getUserProfile(user_id : int):

    access_token = get_jwt_identity()
    user : UserModel = UserModel.query.filter_by(
        id = user_id, email = access_token).first()

    if user:
        return jsonify({
            "name" : user.name,
            "email" : user.email,
            "bio" : user.bio
        }), 200
        
    return jsonify({
        "message" : "User does not Exists",
        "status" : 404
    }), 404


@USER_API.route("/<int:user_id>/", methods=["POST"])
@jwt_required()
def updateUserPassword(user_id : int):

    access_token = get_jwt_identity()
    user : UserModel = UserModel.query.filter_by(
        id = user_id,
        email = access_token
    ).first()

    if user:
        old_password = request.form["old_password"]
        new_password = request.form["new_password"]

        if BCRYPT.check_password_hash(user.password, old_password):
            user.password = BCRYPT.generate_password_hash( new_password )
            DB.session.commit()

            return jsonify({
                "message" : "Successfully Updated Password",
                "status" : 200
            }), 200
        else:
            return jsonify({
                "message" : "Incorrect Password",
                "status" : 400
            }), 400
        
    return jsonify({
        "message" : "User does not Exists",
        "status" : 404
    }), 404


@USER_API.route("/<int:user_id>/", methods=["PUT"])
@jwt_required()
def updateUserProfile(user_id : int):

    access_token = get_jwt_identity()
    user : UserModel = UserModel.query.filter_by(
        id = user_id, email = access_token
    ).first()

    if user:
        data = request.get_json()
        
        name = None if data["name"] is None else data["name"]
        bio = None if data["bio"] is None else data["bio"]

        if name is not None and len(name) < 4:
            return jsonify({
                "message" : "Invalid Name",
                "status" : 400
            }), 400
        
        if name is not None:
            user.name = name

        if bio is not None:
            user.bio = bio
    
        DB.session.commit()
        return jsonify({
            "message" : "Successfully Update Profile",
            "status" : 200
        }), 200

    return jsonify({
        "message" : "User does not Exists",
        "status" : 404
    }), 404


@USER_API.route("/<int:user_id>/", methods=["DELETE"])
@jwt_required()
def deleteUser(user_id : int):

    access_token = get_jwt_identity()
    user : UserModel = UserModel.query.filter_by(
        id = user_id,
        email = access_token
    ).first()

    if user:

        response = jsonify({
            "message" : "Successfully Deleted User",
            "status" : 200
        })
        unset_jwt_cookies(response)
        unset_access_cookies(response)

        DB.session.delete(user)
        DB.session.commit()

        return response, 200
    
    return jsonify({
        "message" : "User does not Exists",
        "status" : 404
    }), 404

