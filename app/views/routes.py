from flask import Blueprint, request, session, render_template, redirect, url_for
from app.models import Users
from app.database import db

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
  return render_template('home.html')

@bp.route("/report")
def summary():
  return render_template('summary.html')

@bp.route("/signup", methods=['GET','POST'])
def signup():
  if request.method == 'POST':
    new_user = Users(
        email=request.form['email'],
        password=request.form['password'],
        username=request.form['username'])
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('main.login'), code=200)
  return render_template('signup.html')

@bp.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    data = Users.query.filter_by(email=email, password=password).first()
    if data is not None:
      session['email'] = email
      return redirect(url_for('main.home'), code=200)
    else:
      return "[ERROR!] 'email' 또는 'password'가 일치하지 않습니다"
  return render_template('login.html')

@bp.route("/logout", methods=['GET'])
def logout():
  session.pop('email', None)
  return redirect('/')