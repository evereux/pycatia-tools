from flask import render_template

from application import app
from application.pycatia_scripts.product.tree import reorder_tree
from application.views.url_prefixes import htmx


@app.route(f'{htmx}/product/reorder_tree', methods=['POST'])
def htmx_reorder_tree():
    r = reorder_tree()

    if r:
        return '<p class="alert alert-success">Product Tree has been reordered.</p>'

    return render_template('partials/error.html')
