from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

# Initializing application
app = Flask(__name__)
app.config.from_object(DevConfig)
from app import views #routes 

# Initializing Flask Extensions
bootstrap = Bootstrap(app)