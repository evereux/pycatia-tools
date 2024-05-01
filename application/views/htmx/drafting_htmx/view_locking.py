from flask import request

from application import app
from application.support.template import render_template
from application.views.url_prefixes import htmx
from application.pycatia_scripts.drafting.view_locking import view_locker


@app.route(f'{htmx}/drafting/locking', methods=['POST'])
def htmx_drafting_locking():
    locker = request.form.get('locker') or None
    inc_main_view = request.form.get('includeMainViewLock', type=bool) or False
    inc_background_view = request.form.get('includeBackgroundViewLock', type=bool) or False

    if locker == 'lock':
        lock = True
    else:
        lock = False

    output = view_locker(lock, inc_main_view, inc_background_view)
    data = output['data']
    errors = output['errors']

    if errors:
        return render_template('partials/errors.html', errors=errors)

    if data:
        return render_template('partials/success.html', data=data)

    return render_template('partials/error.html')
