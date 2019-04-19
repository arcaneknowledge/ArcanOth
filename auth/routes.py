from flask import (
    render_template, url_for, request,
    redirect, flash
)
from auth import auth_bp
from forms import *

@auth_bp.route('/login', methods=['GET', 'POST'])
def login_page():
    #form = LoginForm()
    return render_template('forms/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register_page():
    #form = RegisterForm()
    return render_template('forms/register.html')
