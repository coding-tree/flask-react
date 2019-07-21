from flask import Blueprint, request, jsonify
from flask_login import login_user, current_user

from server.models import Ticket, User, Replies, ticket_replies
from server import db

support =  Blueprint('support', __name__)

@support.route('/api/support/tickets', methods=['GET'])
def user_tickets():
    login_user(User(username='LSD', password='chujkurwa'))
    user = User.query.filter_by(username='LSD').first()
    data = []
    for ticket in user.tickets:
        data.append(dict(account={
            'subject': ticket.subject,
            'status': ticket.status,
            'message': ticket.message,
            'confirmed': ticket.created_on.strftime("%Y/%m/%d, %H:%M:%S")
         }))
    return jsonify(data)

@support.route('/api/support/new-ticket', methods=['POST'])
def create_ticker():
    login_user(User(username='LSD', password='chujkurwa'))
    user = User.query.filter_by(username='LSD').first()

    subject = request.json.get('subject')
    message = request.json.get('message')

    ticket = Ticket(subject=subject, message=message)

    user.tickets.append(ticket)
    db.session.commit()
    return 'ok'

@support.route('/api/support/detail/<ticket_id>', methods=['GET'])
def ticket_details(ticket_id):
    ticket = Ticket.query.filter_by(id=ticket_id).first_or_404()
    for reply in ticket.replies:
        print(reply.reply)
        print(reply.reply_user)
    return 'ok'

@support.route('/api/support/reply/<ticket_id>', methods=['POST'])
def ticket_reply(ticket_id):
    login_user(User(username='LSD55', password='chujkurwa'))
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    message = request.json.get('message')
    reply = Replies(reply=message, reply_user=current_user.username)
    ticket.replies.append(reply)
    db.session.commit()

    return 'ok'