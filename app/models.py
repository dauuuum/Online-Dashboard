from app.database import db
from sqlalchemy import Column, Integer, String, ForeignKey

class Users(db.Model):
  __tablename__ = 'users'

  email = db.Column(db.String(32), primary_key = True)
  password = db.Column(db.String(32))
  username = db.Column(db.String(32))