from flask import (
    render_template, url_for, request,
    redirect, flash
)
from auth import auth_bp
from forms import *

@auth_bp('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    return render_template('forms/login.html', form=form)

@auth_bp('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    return render_template('forms/register.html', form=form)
