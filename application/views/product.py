from application import app
from application.support.properties import get_properties
from application.support.documents import get_product_document
from application.support.template import render_template
from application.views.view_wrappers import catia_v5_required


@app.route('/product')
@catia_v5_required
def product():
    return render_template(
        'product.html',
    )


@app.route('/product/new')
@catia_v5_required
def product_new():

    default_properties = get_properties(None, 'default')
    user_defined_properties = get_properties(None, 'user')

    return render_template(
        'product_new.html',
        default_properties=default_properties,
        user_defined_properties=user_defined_properties
    )


@app.route('/product/reorder')
@catia_v5_required
def product_reorder():
    return render_template(
        'product_reorder.html',
    )


@app.route('/product/renumber_instances')
@catia_v5_required
def product_renumber_instances():
    return render_template(
        'product_renumber_instances.html',
    )


@app.route('/product/properties')
@catia_v5_required
def product_properties():
    pt_product_document, errors = get_product_document(product_only=False)

    if errors:
        return render_template('partials/errors.html', errors=errors)

    product = pt_product_document.product

    default_properties = get_properties(product, 'default')
    user_defined_properties = get_properties(product, 'user')

    return render_template(
        'product_properties.html',
        default_properties=default_properties,
        user_defined_properties=user_defined_properties,
    )
