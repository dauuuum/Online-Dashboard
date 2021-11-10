from flask import Blueprint
from app.models import Users

bp = Blueprint("main", __name__)

@bp.route("/")
def main():
  return "hello"