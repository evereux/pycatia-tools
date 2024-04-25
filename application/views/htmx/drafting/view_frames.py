from flask import request

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

    r = view_framer(frame)

    if r:
        return '<p class="alert alert-success">Frame request processed!</p>'
    else:
        return '<p class="alert alert-warning">The was a problem.</p>'
