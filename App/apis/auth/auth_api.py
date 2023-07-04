from App.models import UserModel, TokenModel
from App.utils import isValidEmail
from App import DB, BCRYPT

from flask_restful import (
    Resource, 
    reqparse, 
    abort
)
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

        if not isValidEmail(data["email"]):
            abort(401, message="Invalid Email Address")

        user : UserModel = UserModel.query.filter_by(email = data["email"]).first()
        if user:
            if not BCRYPT.check_password_hash(user.password, data["password"]):
                abort(401, message="Incorrect Password")
            
            access_token = create_access_token(identity=user.email)  
            refresh_token = create_refresh_token(identity=user.email)  
            
            return {
                "message" : "User logged in successfully",
                "access_token" : access_token,
                "refresh_token" : refresh_token,
                "user" : user.toObject()
            }, 200
            
        abort(404, mesage="User does not Exists")
            

class SignUpResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("username", type=str, required=True)
        self.parser.add_argument("email", type=str, required=True)
        self.parser.add_argument("password", type=str, required=True)
        

    def post(self):
        data = self.parser.parse_args()

        if not isValidEmail(data["email"]):
            abort(401, message="Invalid Email Address")

        user : UserModel = UserModel.query.filter_by(
            username = data["username"],
            email = data["email"]
        ).first()

        if user:    
            abort(409, message="User already exists") 

        if len(data["username"]) < 4:
            abort(401, message="Username must at least be 4 characters long")

        if len(data["password"]) < 6:
            abort(401, message="Password must at least be 6 characters long")

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
            abort(500, message=e)
    

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
            abort(500, message=e)
        

class RefreshTokenResource(Resource):
    
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user)
        
        return {"access_token" : new_token}, 200