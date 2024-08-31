from mongoengine import Document
from mongoengine.fields import StringField


class User(Document):
    meta = {'collection': 'user'}
    first_name = StringField(required=True)
    last_name = StringField(required=True)
