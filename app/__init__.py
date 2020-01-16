from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from dotenv import load_dotenv
from app.models.shared import db

def create_app():

    # Construct the application
    app = Flask(__name__, instance_relative_config=False)
    
    #load_dotenv()
    app.config.from_object('config.Config')
    db.init_app(app)

    # Register schemas
    from app.models.product import Product
    # Register routes
    from app.routes.product_routes import product_api
    app.register_blueprint(product_api)

    return app
