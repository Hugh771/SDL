from functools import wraps
from flask_jwt_extended import JWTManager,get_jwt_identity,get_jwt

jwt = JWTManager()

#权限信息封装
@jwt.additional_claims_loader
def add_claims_to_access_token(identity):
    pass

#权限检验
def user_required(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
         identity = get_jwt_identity()

