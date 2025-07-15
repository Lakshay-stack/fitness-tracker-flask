from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'  # Clearer table name

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    # Fitness profile fields
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))        # 'Male', 'Female', 'Other'
    weight = db.Column(db.Float)             # kg
    height = db.Column(db.Float)             # cm
    body_fat = db.Column(db.Float)           # %
    routine = db.Column(db.String(200))      # e.g., "4 days/week + cardio"
    goal = db.Column(db.String(100))         # e.g., "Lose Fat"

    def __repr__(self):
        return f'<User {self.username}>'
