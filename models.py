from . import db
from flask_login import UserMixin


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    sleep_start = db.Column(db.Time, nullable=False)
    sleep_end = db.Column(db.Time, nullable=False)
    sleep_duration = db.Column(db.Interval, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    exercise = db.Column(db.Boolean, nullable=False)
    breakfast = db.Column(db.Boolean, nullable=False)
    lunch = db.Column(db.Boolean, nullable=False)
    dinner = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    info = db.relationship('Info')
