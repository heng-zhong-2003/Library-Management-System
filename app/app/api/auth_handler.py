from flask import Blueprint, request
from ..models.user import User
from ..models import db
from ..response import *

auth_handler = Blueprint(
    name='auth_handler',
    import_name=__name__,
    url_prefix='/api/auth'
)

@auth_handler.route(rule='/register', methods=['POST'])
def auth_register():
    data = request.get_json(force=True)
    email = data.get('email', None)
    name = data.get('name', None)
    password = data.get('password', None)
    if email is None or password is None or name is None:
        return bad_request(msg='Missing Field(s)')
    user = User.create(
        email=email,
        name=name,
        password=password
    )
    if user is None:
        return bad_request(msg='Invalid: Email already exists')
    ret = user.serialize()
    return response_ok(data=ret)

@auth_handler.route(rule='/login', methods=['POST'])
def auth_login():
    # print('ok')
    data = request.get_json(force=True)
    email = data.get('email', None)
    password = data.get('password', None)
    print(email, password)
    user = User.query.filter(
        User.email == email,
        User.password == password
    ).first()
    if user is None:
        return bad_request(msg='Incorrect email or password')
    ret = user.serialize()
    return response_ok(data=ret)
