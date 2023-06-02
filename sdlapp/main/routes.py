from flask import redirect,render_template,url_for,jsonify
from . import main_bp

@main_bp.route('/login')
def login():
    return jsonify({'hello':1})

@main_bp.route('/logout')
def louout():
    return jsonify({'hello':1})