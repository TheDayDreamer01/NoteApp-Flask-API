from App.utils.regexps_util import isValidEmail
from App.models import UserModel
from App.app import DB, BCRYPT
from flask import (
    Blueprint, 
    jsonify,
    request
)
from flask_jwt_extended import (
    set_refresh_cookies,
    set_access_cookies,
    create_refresh_token,
    create_access_token,
    unset_jwt_cookies,
    jwt_required,
    get_jwt_identity
)


AUTH_API : Blueprint = Blueprint("AUTH_API", __name__)


@AUTH_API.route("/signup/", methods=["POST"])
def signUpUser():
    try:
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        user = UserModel.query.filter_by(email=email).first()

        if user:
            return jsonify({
                "message": "User already exists",
                "status": 400,
                "auth": False
            }), 400

        if len(name) < 4:
            return jsonify({
                "message": "Name must contain at least 4 characters",
                "status": 400,
                "auth": False
            }), 400

        if not isValidEmail(email):
            return jsonify({
                "message": "Invalid Email Address",
                "status": 400,
                "auth": False
            }), 400

        if len(password) < 6:
            return jsonify({
                "message": "Password must contain at least 6 characters",
                "status": 400,
                "auth": False
            }), 400

        user = UserModel(
            name=name,
            email=email,
            password=BCRYPT.generate_password_hash(password)
        )

        access_token = create_access_token(identity=email)
        refresh_token = refresh_token(identity = email)
        response = jsonify({
            "auth": True,
            "access_token" : access_token,
            "message": "Authorized Access",
            "status": 200,
        })
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        DB.session.add(user)
        DB.session.commit()
    
    except Exception as e:
        return jsonify({
            "error" : e,
            "message" : "Internal Server Error",
            "status" : 500
        }), 500

    return response, 200


@AUTH_API.route("/signin/", methods=["POST"])
def signInUser():
    try:
        email = request.form["email"]
        password = request.form["password"]

        user = UserModel.query.filter_by(email = email).first()

        if user:
            if BCRYPT.check_password_hash(user.password, password):
                access_token = create_access_token(identity=email)
                refresh_token = create_refresh_token(identity=email)
                response = jsonify({
                    "auth": True,
                    "access_token" : access_token,
                    "message": "Authorized Access",
                    "status": 200,
                })
                set_access_cookies(response, access_token)
                set_refresh_cookies(response, refresh_token)

                return response, 200
            
            return jsonify({
                "auth": False,
                "message": "Incorrect Password",
                "status": 400,
            }), 400
        
    except Exception as e:
        return jsonify({
            "error" : e,
            "message" : "Internal Server Error",
            "status" : 500
        }), 500
    
    return jsonify({
        "auth": False,
        "message": "User does not Exists",
        "status": 404,
    }), 404


@AUTH_API.route("/signout/", methods=["POST"])
def signOutUser():
    response = jsonify({
        "message" : "Successfully Logged Out",
        "status" : 200
    })
    unset_jwt_cookies(response)
    return response, 200 


@AUTH_API.route("/refresh/", methods=["POST"])
@jwt_required(refresh=True)
def refreshAccessToken():
    try:
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()

        if user:
            new_token = create_access_token(identity=access_token)
            response = jsonify({
                "message" : "Refreshed Access Token",
                "access_token" : new_token,
                "status" : 200
            })
            set_access_cookies(response, new_token)
            return response, 200
    
    except:
        return jsonify({
            "message" : "Internal Server Error",
            "status" : 500
        }), 500
    

    return jsonify({
        "message" : "User does not Exists",
        "status" : 404
    }), 404