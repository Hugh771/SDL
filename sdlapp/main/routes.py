from flask import redirect,render_template,url_for,jsonify,request
from . import main_bp
from flask_jwt_extended import jwt_required,create_access_token
from sdlapp.auth.auth import jwt,permissions_required

@main_bp.route('/login')
def login():
    # if request.method == 'GET':
    #     render_template()
    # if request.method == 'POST':
    #     json = request.get_json()
    #     if json['username'] == 'Jason' and json['passwd'] == '123':
    #         return jsonify({'login':1})
    access_token = create_access_token(identity='admin')
    return jsonify(access_token=access_token),200
@main_bp.route('/view')
@jwt_required()
@permissions_required
def view():
    return jsonify({'view':1})

@main_bp.route('/logout')
@jwt_required()
@permissions_required
def louout():
    return jsonify({'logout':1})