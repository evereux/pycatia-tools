from flask import request, render_template

from application import app
from application.views.url_prefixes import htmx
from application.pycatia_scripts.drafting.view_frames import view_framer


@app.route(f'{htmx}/drafting/frames', methods=['POST'])
def htmx_drafting_framing():
    framer = request.form.get('framer') or None

    if framer == "on":
        frame = True
    else:
        frame = False

    output = view_framer(frame)
    data = output['data']
    errors = output['errors']

    if errors:
        return render_template('partials/errors.html', errors=errors)

    if data:
        return render_template('partials/success.html', data=data)

    return render_template('partials/error.html')
