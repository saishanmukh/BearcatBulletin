from xml.etree.ElementInclude import include
from sqlalchemy import true
from app.ma import ma
from marshmallow import post_load, pre_dump, post_dump, pre_load
from marshmallow import fields
from flask import request

from marshmallow import validate


from app.models.news import News
from app.schemas.images import ImagesSchema

class NewsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = News
        fields = ("news_id", "headline", "description", "category", "hashtag", "posted_by", "channel_id", "posted_date", "edited_date", "images")
        dump_only = ("news_id")
    images = fields.Nested(ImagesSchema, many=True, only=("image_path", ))
    # user = fields.Nested("UserSchema", only=('first_name', 'last_name', 'id'))



    # @pre_dump
    # def process_output(self, data, **kwargs):
    #     print(data)
    #     return data

    # @post_dump
    # def process_output(self, data, **kwargs):
    #     print(request.args.getlist("include"))
    #     print(data)
    #     # data['user'] = True
    #     return data

class NewsSchemaWithImages(ma.Schema):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['images'] = True
    id = fields.String(required=True)
    profileImage = fields.Raw(type='file')

    @pre_load
    def process_input(self, data, **kwargs):

        # check if there is a profile image
        if 'profileImage' in request.files:
            data['profileImage'] = request.files['profileImage']
        else:
            # return input fields missing error

            return {'code': 400, 'messages': ['profileImage is required']}, 400
        return data
    # def __init__(self, *args, **kwargs):
        # pass
        # super().__init__(*args, **kwargs)
        # self.fields["images"] = fields.Raw(type='file')

class CreateNewsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = News
        fields = ("news_id", "headline", "description", "category", "hashtag", "posted_by", "channel_id", "posted_date", "edited_date")
        dump_only = ("news_id", )

# class NewsSchemaWithImagesData(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = News
#         fields = ("news_id", "headline", "description", "category", "hashtag", "posted_by", "channel_id", "posted_date", "edited_date")
#         dump_only = ("news_id", )
    # headline = fields.String(required=True)
    # profileImage = fields.Raw(type='file')
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields["images"] = fields.List(fields.Str)
        # self.fields['images'] = fields.Raw(type='file')

    # images = fields.Raw(type='file')

    # class Meta:
    #     model = News
    #     fields = ("news_id", "headline", "description", "category", "hashtag", "posted_by", "channel_id", "posted_date", "edited_date")
    #     dump_only = ("news_id", )

    # headline = fields.Str()
    # data = fields.Dict(keys=fields.Str(), values=fields.Str())
    # pass images to the request
    # @pre_load
    # def pre_load(self, data, **kwargs):
    #     data = data.to_dict(flat=False)
    #     print(data)
    #     # data['images'] = request.files.getlist('images')
    #     # data["headline"] = data["headline"][0]
    #     data["data"] = data["data"][0]
    #     # print(self.get_default_request())
    #     return data


class NewsSchemaFilterArguments(ma.Schema):
    include = fields.List(fields.String(validate=validate.OneOf(["images", "user"])), required=False, \
        default=["images"], description="Include fields in response")

    # @post_load
    # def make_object(self, data, **kwargs):
    #     data['images'] = True
    #     return data

    # @pre_dump
    # def make_object(self, data, **kwargs):
    #     data['images'] = True
    #     print(data)
    #     return data
    
    # @post_dump
    # def make_object(self, data, **kwargs):
    #     data['images'] = True
    #     print(data)
    #     return data

    # @post_load
    # def make_object(self, data, **kwargs):
    #     data['images'] = True
    #     print(data)
    #     return data
    
    # @pre_load
    # def make_object(self, data, **kwargs):
    #     data['images'] = True
    #     print(data)
    #     return data

    


    # def process_include(self, data, **kwargs):
    #     if "include" in data:
    #         if "images" in data["include"]:
    #             data["include"].remove("images")
    #             data["include"].append("images")
    #         if "user" in data["include"]:
    #             data["include"].remove("user")
    #             data["include"].append("user")
    #     return data

