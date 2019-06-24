from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Blueprints (components)
from .ranking.views import ranking

app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
#app.config.from_envvar('APP_CONFIG_FILE')

# Define the database
db = SQLAlchemy(app)

# Register blueprints (components)
app.register_blueprint(ranking)