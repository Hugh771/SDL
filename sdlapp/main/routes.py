from flask import redirect,render_template,url_for,jsonify,request
from . import main_bp
from flask_jwt_extended import jwt_required

@main_bp.route('/login')
def login():
    if request.method == 'GET':
        render_template()
    if request.method == 'POST':
        return jsonify({'login':1})

@main_bp.route('/view')
@jwt_required()
def view():
    return jsonify({'view':1})

@main_bp.route('/logout')
@jwt_required()
def louout():
    return jsonify({'logout':1})