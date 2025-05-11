from tortoise.models import Model
from tortoise import fields

class User(Model):
  id = fields.IntField(primary_key=True)
  name = fields.CharField(max_length=240)
  email = fields.CharField(max_length=200)
  password = fields.TextField()