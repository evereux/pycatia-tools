from flask import render_template

from application import app


@app.errorhandler(403)
def not_found_error(error):
    return render_template('403.html', error=error), 403


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(406)
def not_found_error(error):
    return render_template('406.html', error=error), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500
