from flask import render_template
from app import db
from errors import errors_bp

@errors_bp.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@errors_bp.app_errorhandler(500):
def error_500(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500