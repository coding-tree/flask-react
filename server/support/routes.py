from flask import Blueprint, request, jsonify, abort
from flask_login import login_user, current_user

from server.models import Ticket, User, Replies, ticket_replies
from server import db

support =  Blueprint('support', __name__)

@support.route('/api/support/tickets', methods=['GET'])
def user_tickets():
    login_user(User(username='LSD', password='chujkurwa'))
    user = User.query.filter_by(username=current_user.username).first()
    data = []
    for ticket in user.tickets:
        data.append(dict(ticket={
            'subject': ticket.subject,
            'status': ticket.status,
            'message': ticket.message,
            'date': ticket.created_on.strftime("%Y/%m/%d, %H:%M:%S")
         }))
    return jsonify(data)

@support.route('/api/support/new-ticket', methods=['POST'])
def create_ticker():
    login_user(User(username='LSD55', password='chujkurwa'))
    user = User.query.filter_by(username=current_user.username).first()

    subject = request.json.get('subject')
    message = request.json.get('message')

    if subject and message is None:
        return jsonify({
            'message': 'Pola nie mogą być puste!',
            'category': 'danger'
        })

    ticket = Ticket(subject=subject, message=message)

    user.tickets.append(ticket)
    db.session.commit()
    
    return jsonify({
        'message': 'Twoje zgłoszenie zostało wysłane, prosimy cierpliwie czekać na odpowiedź administratora',
        'category': 'success'
    })

@support.route('/api/support/edit/ticket/<ticket_id>', methods=['GET', 'POST'])
def edit_ticket(ticket_id):
    login_user(User(username='LSD55', password='chujkurwa'))
    user = User.query.filter_by(username=current_user.username).first()
    tickets = Ticket.query.filter_by(id=ticket_id).first()

    allowed_fields = ('subject', 'message')
    __, t_user = str(tickets.user[0]).split(':')
    if t_user == current_user.username:
        print(tickets)
        for field in allowed_fields:
            fieldValue = request.json.get(field)

            if fieldValue is not None:
                setattr(tickets, field, fieldValue)
                db.session.commit()
    else: return abort(404)

    return 'ok'

@support.route('/api/support/close-ticket/<ticket_id>')
def close_ticket(ticket_id):
    login_user(User(username='LSD', password='chujkurwa'))
    user = User.query.filter_by(username=current_user.username).first()
    tickets = Ticket.query.filter_by(id=ticket_id).first()

    allowed_fields = ('subject', 'message')
    __, t_user = str(tickets.user[0]).split(':')
    if t_user == current_user.username or user.gid == 0:
        tickets.status = 'CLOSED'
        db.session.commit()
    else: abort(404)
    
    return jsonify({
        'message': 'Zgłoszenie zostało zamknięte',
        'category': 'info'
    })

@support.route('/api/support/detail/<ticket_id>', methods=['GET'])
def ticket_details(ticket_id):
    data = []
    ticket = Ticket.query.filter_by(id=ticket_id).first_or_404()
    for reply in ticket.replies:
        data.append(dict(reply={
            'message': reply.reply,
            'user': reply.reply_user,
            'date': reply.reply_on.strftime("%Y/%m/%d, %H:%M:%S")
         }))
    return jsonify(data)

@support.route('/api/support/reply/<ticket_id>', methods=['POST'])
def ticket_reply(ticket_id):
    login_user(User(username='LSD55', password='chujkurwa'))
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    if ticket is 'CLOSED':
        return jsonify({
            'message': 'Ten wątek jest zamknięty i nie można odpowiedzieć',
            'category': 'warning'
        })
    message = request.json.get('message')
    reply = Replies(reply=message, reply_user=current_user.username)
    ticket.replies.append(reply)
    db.session.commit()

    return jsonify({
        'message': 'Pomyślnie wysłano odpowiedź',
        'category': 'success'
    })