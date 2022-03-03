# -*- coding: utf-8 -*-

from peewee import *
from datetime import datetime

db = SqliteDatabase("data.sqlite3")

class BaseModel(Model):
    class Meta:
        database = db

class IoT(BaseModel):
    model=CharField()
    serie=CharField()
    mac=CharField()
    active=BooleanField(default=True)
