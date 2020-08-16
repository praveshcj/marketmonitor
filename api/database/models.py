from .db import db

class Company(db.Document):
    name = db.StringField(required=True, unique=True)
    security_key = db.ListField(db.StringField(), required=True)
    macd25 = db.DecimalField()
    macd9  = db.DecimalField()

class Record(db.Document):
    company = db.ReferenceField(Company)
    date = db.DateTimeField()
    opening = db.DecimalField()
    closing = db.DecimalField()