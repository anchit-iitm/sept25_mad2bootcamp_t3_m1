from flask import Flask
from flask_security import Security

from models import db
from routes import api
from route import app_api



def create_app():
    init_app = Flask(__name__)
    from config import DevelopmentConfig
    init_app.config.from_object(DevelopmentConfig)

    db.init_app(init_app)
    api.init_app(init_app)

    init_app.register_blueprint(app_api, url_prefix='/api')

    from models import user_datastore
    Security(init_app, user_datastore)

    return init_app

app = create_app()

if __name__ == "__main__":
    app.run()