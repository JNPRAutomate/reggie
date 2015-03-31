from datetime import datetime
from flask import current_app, request
from . import db

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    pod_number = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(64), unique=True)
    wan_ip = db.Column(db.String(16), unique=True)
