from application import app
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
    return render_template(
        'product_new.html',
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


@app.route('/product/attributes')
@catia_v5_required
def product_attributes():
    pt_product_document, errors = get_product_document()

    if errors:
        return render_template('partials/errors.html', errors=errors)

    product = pt_product_document.product

    attributes = {
        'part_number': product.part_number,
    }

    return render_template(
        'product_attributes.html',
        attributes=attributes
    )
