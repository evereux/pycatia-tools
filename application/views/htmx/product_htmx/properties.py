from flask import request

from application import app
from application.support.documents import get_product_document
from application.support.properties import update_properties, get_properties
from application.support.template import render_template
from application.views.url_prefixes import htmx


@app.route(f'{htmx}/product/properties', methods=['POST'])
def htmx_product_properties():

    pt_product_document, errors = get_product_document(product_only=False)
    product = pt_product_document.product

    update_properties(product, request.form)

    default_properties = get_properties(product, 'default')
    user_defined_properties = get_properties(product, 'user')

    return render_template(
        'partials/form_product_properties.html',
        default_properties=default_properties,
        user_defined_properties=user_defined_properties
    )
