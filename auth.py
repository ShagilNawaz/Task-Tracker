from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data["username"] == "admin" and data["password"] == "admin":
        return jsonify({"token": "fake-jwt-token"})
    return jsonify({"error": "Invalid credentials"}), 401