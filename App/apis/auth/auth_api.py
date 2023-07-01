from App.models import UserModel, TokenModel
from App.app import DB, BCRYPT

from flask_restful import Resource, reqparse, abort
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
                return {"message": "Incorrect Password"}, 401
            
            access_token = create_access_token(identity=user.email)  
            refresh_token = create_refresh_token(identity=user.email)  
            
            return {
                "message" : "User logged in successfully",
                "access_token" : access_token,
                "refresh_token" : refresh_token,
                "user" : user.toObject()
            }, 200
            
        return {"message" : "User does not Exists"}, 404
            

class SignUpResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("username", type=str, required=True)
        self.parser.add_argument("email", type=str, required=True)
        self.parser.add_argument("password", type=str, required=True)
        

    def post(self):
        data = self.parser.parse_args()

        user : UserModel = UserModel.query.filter_by(
            username = data["username"],
            email = data["email"]
        ).first()

        if user:    
            return abort(409, message="User already exists") 

        user = UserModel(
            username = data["username"],
            email = data["email"],
            password = BCRYPT.generate_password_hash(data["password"])
        )

        access_token = create_access_token(identity=data["email"])
        refresh_token = create_refresh_token(identity=data["email"])
        DB.session.add(user)
        DB.session.commit()

        return {
            "message" : "User created successfully",
            "access_token" : access_token,
            "refresh_token" : refresh_token,
            "user" : user.toObject()
        }, 201
   
        
class SignOutResource(Resource):

    @jwt_required(optional=True)
    def post(self):
        try:    
            access_token = get_jwt()["jti"]
            token : TokenModel = TokenModel(token = access_token)

            DB.session.add(token)
            DB.session.commit()

            return {"message" : "Successfully logged out"}, 200
    
        except Exception as e:
            return {"message" : e}, 500
    

class SignOutRefreshResource(Resource):

    @jwt_required(refresh=True)
    def post(self):
        try:
            access_token = get_jwt()["jti"]
            token : TokenModel = TokenModel(token = access_token)
            
            DB.session.add(token)
            DB.session.commit()
            return {"message" : "Successfully logged out"}, 200
    
        except Exception as e:
            return {"message" : e}, 500
        

class RefreshTokenResource(Resource):
    
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user)
        
        return {"access_token" : new_token}, 200