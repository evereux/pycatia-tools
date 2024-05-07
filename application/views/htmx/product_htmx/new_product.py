from flask import request

from application import app
from application.pycatia_scripts.product.new_product import create_new_product
from application.support.template import render_template
from application.views.url_prefixes import htmx


@app.route(f'{htmx}/product/create_new', methods=['POST'])
def htmx_create_new_product():
    part_number = request.form.get('part_number', type=str) or False
    revision = request.form.get('revision', type=str) or False
    definition = request.form.get('definition', type=str) or False
    nomenclature = request.form.get('nomenclature', type=str) or False

    r = create_new_product(part_number, revision, definition, nomenclature)

    if r:
        return f'<p class="alert alert-success">New Product "{part_number}" created.</p>'

    return render_template('partials/error.html')
