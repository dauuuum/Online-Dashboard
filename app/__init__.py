from flask import Flask
from app.database import db, migrate

def create_app():
  app = Flask(__name__)
  app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://fixvzxjd:Wxh0m3L_bopzUCp79LukrFMQ4JLaupgN@rosie.db.elephantsql.com/fixvzxjd"
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  db.init_app(app)
  migrate.init_app(app, db)

  from .views.routes import bp
  app.register_blueprint(bp)

  return app

if __name__ == "__main__":
  app = create_app()
  app.run(debug=True)