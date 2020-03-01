from flask import redirect, render_template

from app.errors import bp

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404
