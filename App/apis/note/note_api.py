from flask import (
    Blueprint,
    request,
    jsonify
)

from flask_jwt_extended import (
    get_jwt_identity,
    set_access_cookies,
    jwt_required
)


NOTE_API : Blueprint = Blueprint("NOTE_API", __name__)


@NOTE_API.route("/api/note/<int:user_id>/", methods=["GET"])
def getNote(user_id : int):

    return jsonify({
        "message" : "Hello World"
    })