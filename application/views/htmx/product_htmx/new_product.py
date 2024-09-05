from flask import request

from application import app
from application.pycatia_scripts.product.new_product import create_new_product
from application.support.documents import get_product_document
from application.support.properties import get_properties
from application.support.template import render_template
from application.views.url_prefixes import htmx


@app.route(f'{htmx}/product/create_new', methods=['POST'])
def htmx_create_new_product():

    output = create_new_product(request.form)
    data = output['data']
    errors = output['errors']

    pt_product_document, errors = get_product_document()
    product = pt_product_document.product

    default_properties = get_properties(product, 'default')
    user_defined_properties = get_properties(product, 'user')

    return render_template(
        'partials/form_product_properties.html',
        default_properties=default_properties,
        user_defined_properties=user_defined_properties,
        data=data,
        errors=errors
    )
