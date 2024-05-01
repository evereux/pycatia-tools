from flask import request

from application import app
from application.support.documents import get_product_document
from application.support.template import render_template
from application.views.url_prefixes import htmx


@app.route(f'{htmx}/product/attributes', methods=['GET', 'PUT'])
def htmx_attributes():

    pt_product_document, errors = get_product_document()
    product = pt_product_document.product

    attributes = {
        'part_number': product.part_number,
        'revision': product.revision,
        'definition': product.definition,
        'nomenclature': product.nomenclature
    }

    if request.method == 'PUT':
        product.part_number = request.form.get('part_number', type=str)
        product.revision = request.form.get('revision', type=str)
        product.definition = request.form.get('definition', type=str)
        product.nomenclature = request.form.get('nomenclature', type=str)

    if not errors:
        return render_template('partials/product_attributes_div.html', attributes=attributes)
    else:
        return render_template('partials/errors.html', errors=errors)


@app.route(f'{htmx}/product/attributes/edit', methods=['GET'])
def htmx_attributes_edit():

    pt_product_document, errors = get_product_document()
    product = pt_product_document.product

    attributes = {
        'part_number': product.part_number,
        'revision': product.revision,
        'definition': product.definition,
        'nomenclature': product.nomenclature
    }

    if not errors:
        return render_template('partials/product_attributes_form.html', attributes=attributes)
    else:
        return render_template('partials/errors.html', errors=errors)

    return render_template('partials/error.html')
