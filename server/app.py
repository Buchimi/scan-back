from flask import Flask
from flask_migrate import Migrate
from routes.blueprint import blueprint
from models.machine import db


def create_app():
    app = Flask(__name__) 
    # app.config.from_object('config')  # Configuring from Python Files

    db.init_app(app)
    return app


app = create_app()
# Registering the blueprint
app.register_blueprint(blueprint)
# migrate = Migrate(app, db)  # Initializing the migration


if __name__ == '__main__':
    app.run()