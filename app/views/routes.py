from flask import Blueprint, render_template
from app.models import Users

bp = Blueprint("main", __name__)

@bp.route("/")
def main():
  return render_template('home.html')

@bp.route("/report")
def summary():
  return render_template('summary.html')
