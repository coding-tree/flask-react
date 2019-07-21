from flask import render_template, Blueprint, request, flash, jsonify
from flask_login import current_user

from server.settings import Discord

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    auth = request.headers.get("X-Api-Key").decode()
    if auth == 'lsdkkapp':
        return jsonify({"message": "OK: Authorized"}), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401
