from application import app
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
