from application import app
from application.pycatia_scripts.product.renumber import main
from application.views.url_prefixes import htmx


@app.route(f'{htmx}/product/renumber_instances', methods=['POST'])
def htmx_renumber_instances():
    try:
        r = main()
    except:
        r = False

    if r:
        return '<p class="alert alert-success">Instances have been renumbered.</p>'
    else:
        return '<p class="alert alert-warning">Could not renumber instances. Is the active Document a CATProduct?</p>'
