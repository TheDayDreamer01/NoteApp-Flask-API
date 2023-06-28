from App.models import UserModel
from App.app import DB, BCRYPT
from flask import jsonify
from flask_restful import (
    Resource,
    reqparse,
    abort
)
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)


class UserResource(Resource):
    def __init__(self):
        pass


    @jwt_required
    def get(self, user_id : int):
        pass
    
    
    @jwt_required
    def post(self, user_id : int):
        pass

    
    @jwt_required
    def put(self, user_id : int):
        pass


    @jwt_required
    def delete(self, user_id : int):
        pass




# @USER_API.route("/<int:user_id>/", methods=["GET"])
# @jwt_required()
# def getUserProfile(user_id : int):
#     try:
#         access_token = get_jwt_identity()
#         user : UserModel = UserModel.query.filter_by(
#             id = user_id, email = access_token).first()

#         if user:
#             return jsonify({
#                 "user" : user.toObject(), 
#                 "status" : 200
#             }), 200
        
#     except Exception as e:
#         return jsonify({
#             "error" : e,
#             "message" : "Internal Server Error",
#             "status" : 500
#         }), 500
            
#     return jsonify({
#         "message" : "User does not Exists",
#         "status" : 404
#     }), 404


# @USER_API.route("/<int:user_id>/", methods=["POST"])
# @jwt_required()
# def updateUserPassword(user_id : int):
#     try:
#         access_token = get_jwt_identity()
#         user : UserModel = UserModel.query.filter_by(
#             id = user_id,
#             email = access_token
#         ).first()

#         if user:
#             old_password = request.form["old_password"]
#             new_password = request.form["new_password"]

#             if BCRYPT.check_password_hash(user.password, old_password):
#                 user.password = BCRYPT.generate_password_hash( new_password )
#                 DB.session.commit()

#                 return jsonify({
#                     "message" : "Successfully Updated Password",
#                     "status" : 200
#                 }), 200
#             else:
#                 return jsonify({
#                     "message" : "Incorrect Password",
#                     "status" : 400
#                 }), 400
            
#     except Exception as e:
#         return jsonify({
#             "error" : e,
#             "message" : "Internal Server Error",
#             "status" : 500
#         }), 500
        
#     return jsonify({
#         "message" : "User does not Exists",
#         "status" : 404
#     }), 404


# @USER_API.route("/<int:user_id>/", methods=["PUT"])
# @jwt_required()
# def updateUserProfile(user_id : int):
#     try:
#         access_token = get_jwt_identity()
#         user : UserModel = UserModel.query.filter_by(
#             id = user_id, email = access_token
#         ).first()

#         if user:
#             data = request.get_json()
#             name = data["name"]
#             bio = bio["bio"]

#             if not name:
#                 if len(name) < 4:
#                     return jsonify({
#                         "message" : "Invalid Name",
#                         "status" : 400
#                     }), 400
#                 user.name = name

#             if not bio:
#                 user.bio = bio
        
#             DB.session.commit()
#             return jsonify({
#                 "message" : "Successfully Updated Profile",
#                 "status" : 200
#             }), 200
        
#     except Exception as e:
#         return jsonify({
#             "error" : e,
#             "message" : "Internal Server Error",
#             "status" : 500
#         }), 500

#     return jsonify({
#         "message" : "User does not Exists",
#         "status" : 404
#     }), 404


# @USER_API.route("/<int:user_id>/", methods=["DELETE"])
# @jwt_required()
# def deleteUser(user_id : int):
#     try:
#         access_token = get_jwt_identity()
#         user : UserModel = UserModel.query.filter_by(
#             id = user_id,
#             email = access_token
#         ).first()

#         if user:
#             response = jsonify({
#                 "message" : "Successfully Deleted User",
#                 "status" : 200
#             })
#             unset_jwt_cookies(response)
#             DB.session.delete(user)
#             DB.session.commit()

#             return response, 200
        
#     except Exception as e:
#         return jsonify({
#             "error" : e,
#             "message" : "Internal Server Error",
#             "status" : 500
#         }), 500
    
#     return jsonify({
#         "message" : "User does not Exists",
#         "status" : 404
#     }), 404

