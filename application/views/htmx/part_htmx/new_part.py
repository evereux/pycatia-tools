from flask import request, render_template

from application import app
from application.pycatia_scripts.part.new_part import create_new_part
from application.support.documents import get_product_document
from application.support.properties import get_properties
from application.views.url_prefixes import htmx


@app.route(f'{htmx}/part/create_new', methods=['POST'])
def htmx_create_new_part():
    output = create_new_part(request.form)
    data = output['data']
    errors = output['errors']

    pt_product_document, errors = get_product_document(product_only=False)
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
