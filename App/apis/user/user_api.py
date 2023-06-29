from App.models import UserModel, user_schema
from App.app import DB, BCRYPT

from flask_jwt_extended import jwt_required
from flask_restful import (
    Resource,
    reqparse,
)


class UserResource(Resource):
    def __init__(self):
        self.password_parser = reqparse.RequestParser()
        self.password_parser.add_argument("old_password", type=str, required=True)
        self.password_parser.add_argument("new_password", type=str, required=True)

        self.user_parser = reqparse.RequestParser()
        self.user_parser.add_argument("username", type=str)
        self.user_parser.add_argument("bio", type=str)

    @jwt_required() 
    def get(self, user_id : int):
        user : UserModel = UserModel.query.filter_by(id=user_id).first()
        if not user:
            return {"message" : "User does not exists"}, 404
        
        schema = user_schema.dump(user)
        return {"user" : schema }, 200

    
    @jwt_required()
    def post(self, user_id : int):
        user : UserModel = UserModel.query.filter_by(id=user_id).first()
        if not user:
            return {"message" : "User does not Exists"}, 404
        
        data = self.password_parser.parse_args()

        if not BCRYPT.check_password_hash(user.password, data["old_password"]):
            return {"message" : "Incorrect Password"}, 400
        
        user.password = BCRYPT.generate_password_hash(data["new_password"])
        DB.session.commit()
        return {"message" : "Updated password"}, 200
        
    
    @jwt_required()
    def put(self, user_id : int):
        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            return {"message" : "User does not exists"}, 404
        
        data = self.user_parser.parse_args()

        if data["username"]:
            user.username = data["bio"]
        
        user.bio = data["bio"]
        DB.session.commit()
        return {"message" : "Updated Profile"}, 200


    @jwt_required()
    def delete(self, user_id : int):
        user : UserModel = UserModel.query.filter_by(id=user_id).first()
        if not user:
            return {"message" : "User does not exists"}, 404
        
        DB.session.delete(user)
        DB.session.commit()
        return {"message" : f"User '{user.username}' successfully deleted"}, 200

