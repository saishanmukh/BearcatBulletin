from flask import Blueprint, abort, jsonify, Response
import requests
from apifairy import body, response, other_responses, arguments

from app.models.user import User
from app.schemas.user import UserSchema, UserFilterQueryParamsSchema, UserLoginSchema
from app.schemas import OrderByFilterSchema

USER_NOT_FOUND = "User not found"


user_schema = UserSchema()
users_schema = UserSchema(many=True)


users = Blueprint('users', __name__)

# insert new user
@users.route('/users', methods=['POST'])
@body(UserSchema)
@response(user_schema, 201)
def create_user(user):
    """Create a user"""
    user = User(**user)
    user.save_to_db()
    return user, 201


# retrieve a user by id
@users.route('/users/<int:id>', methods=['GET'])
@response(user_schema, 200)
@other_responses({404: 'User not found.'})
def get_by_id(id):
    """Retrieve a user by id"""
    user = User.find_by_id(id)
    if user:
        return user
    else:
        abort(404, USER_NOT_FOUND)

# delete user by id
@users.route('/users/<int:id>', methods=['DELETE'])
@response(user_schema, 200)
@other_responses({404: 'User not found.'})
def delete_by_id(id):
    """Delete an user by id"""
    user = User.find_by_id(id)
    if user:
        user.delete_from_db()
        # user.save_to_db()
        return user
    else:
        abort(404, USER_NOT_FOUND)

# update user by id
@users.route('/users/<int:id>', methods=['PUT'])
@body(UserSchema)
@response(user_schema, 200)
def update_by_id(id, args):
    """Update an user by id"""
    user = User.find_by_id(id)
    if user:
        user.update(args)
        user.save_to_db()
        return user
    else:
        abort(404, USER_NOT_FOUND)

# login user
@users.route('/users/login', methods=['POST'])
@body(UserLoginSchema)
@response(user_schema, 200)
@other_responses({404: 'User not found.', 401: 'Invalid credentials.'})
def login(args):
    """Login an user"""
    user = User.find_by_email(args['email'])
    if user:
        if user.check_password(args['password']):
            return user
        else:
            abort(Response('Wrong password', 401))
    else:
        print('User not found')
        abort(Response(USER_NOT_FOUND, 404))