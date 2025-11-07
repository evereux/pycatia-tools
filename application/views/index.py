from flask import render_template

from application import app
from application.views.view_wrappers import catia_v5_required


@app.route('/')
@catia_v5_required
def index():
    return render_template('index.html')
