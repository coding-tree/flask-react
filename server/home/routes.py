from flask import render_template, Blueprint, request, flash, jsonify
from flask_login import current_user

from server.settings import Discord

home_bp = Blueprint('home', __name__)



@home_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify('Hello world')

