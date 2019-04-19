from home import home_bp
from flask import (
    render_template, redirect, flash,
    url_for, request
)
from models import *
from forms import *
from config import Config

@home_bp('/')
def home_page():
    return render_template('pages/home.html')
