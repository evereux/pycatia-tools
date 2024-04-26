from flask import request

from application import app
from application.support.template import render_template
from application.views.url_prefixes import htmx
from application.pycatia_scripts.drafting.save_drawing import save_as


@app.route(f'{htmx}/drafting/save_as', methods=['POST'])
def htmx_drafting_save_as():

    exclude = request.form.get('exclude_sheet') or None
    target_directory = request.form.get('target_directory') or None

    output = save_as(exclude_sheets=exclude, target_directory=target_directory)
    data = output['data']
    errors = output['errors']

    if errors:
        return render_template('partials/errors.html', errors=errors)

    if data:
        return render_template('partials/success.html', data=data)

    return '<p class="alert alert-warning">There was a problem.</p>'
