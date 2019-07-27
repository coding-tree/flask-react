from flask import jsonify, Blueprint, request
from flask_login import current_user, login_user
from server.models import User

profile = Blueprint('profile', __name__)

@profile.route('/api/profile/my', methods=['GET', 'POST'])
def curr_user():
    user = User.query.filter_by(username='LSD').first()
    login_user(user)
    user_data = {
        'username': current_user.username,
        'title': current_user.title,
        'email': current_user.email,
        'avatar': current_user.image_file,
        'registered_on': current_user.registered_on,
    }
    return jsonify(user_data)

@profile.route('/api/profile/<username>', methods=['GET'])
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return jsonify(user= {
        'username': user.username,
        'title': user.title,
        'email': user.email,
        'avatar': user.image_file,
        'registered_on': user.registered_on,
    })

@profile.route('/api/accounts', methods=['GET'])
def accounts():
    users = User.query.all()
    data = []
    for user in users:
        data.append(dict(account={
            'username': user.username,
            'email': user.email,
            'registered_on': user.registered_on,
            'confirmed': user.confirmed,
         }))
    return jsonify(data)

@profile.route('/api/account/edit', methods=['GET'])
def update_profile():
    if current_user.is_authenticated:
        newAvatar = request.json.get('av')
        newPassword = request.jeson.get('npass')
        newUsername = request.json.get('nuname')
    else: return 400
