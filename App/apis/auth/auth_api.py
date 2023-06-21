
from App.utils.regexps_util import isValidEmail
from App.models import UserModel
from App.app import DB, BCRYPT
from flask import (
    Blueprint, 
    jsonify,
    request
)
from flask_jwt_extended import (
    set_access_cookies,
    create_access_token,
    unset_jwt_cookies,
    unset_access_cookies
)


AUTH_API : Blueprint = Blueprint("AUTH_API", __name__)


@AUTH_API.route("/signup/", methods=["POST"])
def SignUpUser():
    
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

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
    response = jsonify({
        "message": "Authorized Access",
        "status": 200,
        "auth": True
    })
    set_access_cookies(response, access_token)

    DB.session.add(user)
    DB.session.commit()

    return response, 200


@AUTH_API.route("/signin/", methods=["POST"])
def SignInUser():
    email = request.form["email"]
    password = request.form["password"]

    user = UserModel.query.filter_by(email = email).first()

    if user:
        if BCRYPT.check_password_hash(user.password, password):
            access_token = create_access_token(identity=email)
            response = jsonify({
                "message": "Authorized Access",
                "status": 200,
                "auth": True
            })
            set_access_cookies(response, access_token)
            return response, 200
        
        return jsonify({
            "message": "Incorrect Password",
            "status": 400,
            "auth": False
        }), 400
    
    return jsonify({
        "message": "User does not Exists",
        "status": 404,
        "auth": False
    }), 404


@AUTH_API.route("/signout/", methods=["POST"])
def SignOutUser():
    response = jsonify({
        "message" : "Successfully Logged Out",
        "status" : 200
    })
    unset_jwt_cookies(response)
    unset_access_cookies(response)

    return response
