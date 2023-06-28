from App.models import UserModel, TokenModel
from App.app import DB, BCRYPT
from datetime import timedelta

from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_refresh_token,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)


class SignInResource(Resource):
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("email", type=str, required=True)
        self.parser.add_argument("password", type=str, required=True)


    def post(self):
        data = self.parser.parse_args()

        user : UserModel = UserModel.query.filter_by(email = data["email"]).first()
        if user:
            if not BCRYPT.check_password_hash(user.password, data["password"]):
                return jsonify({"message": "Incorrect Password"}), 401
            
            access_token = create_access_token(
                identity=user.email, expires_delta=timedelta(day=1))  
            refresh_token = create_refresh_token(
                identity=user.email, expires_delta=timedelta(day=1))  
            
            return jsonify({
                "message" : "User logged in successfully",
                "access_token" : access_token,
                "refresh_token" : refresh_token,
                "user" : user.toObject()
            }), 201
            
        return jsonify({"message" : "User does not Exists"}), 404
            

class SignUpResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("username", type=str, required=True)
        self.parser.add_argument("email", type=str, required=True)
        self.parser.add_argument("password", type=str, required=True)
        
    def get(self) : return "HI"
    def post(self):
        data = self.parser.parse_args()

        user : UserModel = UserModel.query.filter_by(
            username = data["username"],
            email = data["email"],
        ).first()

        if not user:    
            return jsonify({"message" : "User already exists"}), 400

        user = UserModel(
            username = data["username"],
            email = data["email"],
            password = BCRYPT.generate_password_hash(data["password"])
        )

        access_token = create_access_token(
            identity=user.email, expires_delta=timedelta(day=1))  
        refresh_token = create_refresh_token(
            identity=user.email, expires_delta=timedelta(day=1))  
        DB.session.add(user)
        DB.session.commit()

        return jsonify({
            "message" : "User created successfully",
            "access_token" : access_token,
            "refresh_token" : refresh_token,
            "user" : user.toObject()
        }), 201
   
        
class SignOutResource(Resource):

    @jwt_required
    def post(self):
        try:
            access_token = get_jwt()

            token : TokenModel = TokenModel(token = access_token)
            DB.session.add(token)
            DB.session.commit()

            return jsonify({"message" : "Successfully logged out"}), 200
    
        except Exception as e:
            return jsonify({"message" : e}), 500
    

class SignOutRefreshResource(Resource):

    @jwt_required(refresh=True)
    def post(self):
        try:
            access_token = get_jwt()

            token : TokenModel = TokenModel(token = access_token)
            DB.session.add(token)
            DB.session.commit()

            return jsonify({"message" : "Successfully logged out"}), 200
    
        except Exception as e:
            return jsonify({"message" : e}), 500
        

class RefreshTokenResource(Resource):
    
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(
            identity=current_user, expires_delta=timedelta(day=1))
        
        return jsonify({"access_token" : new_token}), 200