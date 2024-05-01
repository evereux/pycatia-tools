from flask import request

from application import app
from application.pycatia_scripts.drafting.drawing_template import insert_drawing_template
from application.support.template import render_template
from application.views.url_prefixes import htmx
from application.pycatia_scripts.drafting.view_frames import view_framer


@app.route(f'{htmx}/drafting/template', methods=['POST'])
def htmx_drafting_template():

    part_number = request.form.get('DRAWING-NUMBER', type=str) or False
    title = request.form.get('TITLE', type=str) or False
    drawn_by = request.form.get('DRAWN-BY', type=str) or False
    revision = request.form.get('REVISION', type=str) or False

    form_parameters = {
        'DRAWING-NUMBER': part_number,
        'TITLE': title,
        'DRAWN-BY': drawn_by,
        'REVISION': revision,
    }

    output = insert_drawing_template(form_parameters)
    data = output['data']
    errors = output['errors']

    if errors:
        return render_template('partials/errors.html', errors=errors)

    if data:
        return render_template('partials/success.html', data=data)

    return render_template('partials/error.html')