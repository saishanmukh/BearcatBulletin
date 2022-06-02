from flask import Blueprint, abort, jsonify, Response
from apifairy import body, response, other_responses, arguments

from app.models.user import User
from app.schemas.user import UserSchema, UserFilterQueryParamsSchema, UserLoginSchema, UserSchemaForSignup, UserSchemaForSignupWithToken
from app.schemas import OrderByFilterSchema
from app.utils.mail import send_email
from app.utils.random_password import generate_token

USER_NOT_FOUND = "User not found"


user_schema = UserSchema()
users_schema = UserSchema(many=True)


users = Blueprint('users', __name__)

# insert new user
@users.route('/users', methods=['POST'])
@body(UserSchemaForSignup)
@response(user_schema, 201)
def create_user(user):
    """Create a user"""
    # check if mail contains @nwmissouri.edu
    if not user["email"].endswith('@nwmissouri.edu'):
        return abort(Response(f'Email must end with @nwmissouri.edu', status=400))

    # generate a random token
    user["password"] = generate_token()
    send_email(user["email"], user["password"])
    
    user = User(**user)
    user.save_to_db()
    return user, 201

# validate user token
@users.route('/users/register', methods=['POST'])
@body(UserSchemaForSignupWithToken)
@response(user_schema)
def validate_user_token(user):
    """Sign up user"""
    fetched_user = User.find_by_email(user["email"])
    if not fetched_user:
        return abort(Response(USER_NOT_FOUND, status=400))

    if fetched_user.password != user['otp_code']:
        return abort(Response('Invalid Code', status=400))
    else:
        fetched_user.password = user["password"]
        fetched_user.save_to_db()
        return fetched_user

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