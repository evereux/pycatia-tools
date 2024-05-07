from flask import request

from application import app
from application.pycatia_scripts.part.new_part import create_new_part
from application.support.template import render_template
from application.views.url_prefixes import htmx


@app.route(f'{htmx}/part/create_new', methods=['POST'])
def htmx_create_new_part():

    part_number = request.form.get('part_number', type=str) or False
    revision = request.form.get('revision', type=str) or False
    definition = request.form.get('definition', type=str) or False
    nomenclature = request.form.get('nomenclature', type=str) or False

    r = create_new_part(part_number, revision, definition, nomenclature)

    if r:
        return f'<p class="alert alert-success mt-2">New Part "{part_number}" created.</p>'

    return render_template('partials/error.html')
