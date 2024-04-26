from application import app
from application.support.template import render_template
from application.pycatia_scripts.part.bounding_box import create_bounding_box
from application.views.url_prefixes import htmx


@app.route(f'{htmx}/part/bounding_box', methods=['POST'])
def htmx_bounding_box():

    output = create_bounding_box()
    data = output['data']
    errors = output['errors']

    if errors:
        return render_template('partials/errors.html', errors=errors)

    if data:
        return (f'<p class="alert alert-info mt-3">'
                f'Bounding Box created. '
                f'X={ data["x"] }, '
                f'Y={ data["y"] }, '
                f'Z={ data["z"] }.'
                f'</p>')

    return render_template('partials/error.html')
