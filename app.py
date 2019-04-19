#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import *

import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from auth import auth_bp
app.register_blueprint(auth_bp)
from errors import errors_bp
app.register_blueprint(errors_bp)
from home import home_bp
app.register_blueprint(home_bp)
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

import forms
import models