from flask import Blueprint, abort
from apifairy import body, response, other_responses, arguments


from app.models.channel import Channel
from app.schemas.channel import ChannelSchema


channel_schema = ChannelSchema()
channel_schema_many = ChannelSchema(many=True)


channel = Blueprint('channel', __name__)


# insert new channel
@channel.route('/channel', methods=['POST'])
@body(ChannelSchema)
@response(channel_schema, 201)
def create_channel(channel):
    """Create a channel"""
    channel = Channel(**channel)
    channel.save_to_db()
    return channel, 201

# retrieve a channel by id
@channel.route('/channel/<int:id>', methods=['GET'])
@response(channel_schema, 200)
@other_responses({404: 'Channel not found.'})
def get_by_id(id):
    """Retrieve a channel by id"""
    channel = Channel.find_by_id(id)
    if channel:
        return channel
    else:
        abort(404, 'Channel not found.')

# get all channels
@channel.route('/channel', methods=['GET'])
@response(channel_schema_many)
def get_all():
    """Retrieve all channels"""
    channels = Channel.find_all_channels()
    return channels