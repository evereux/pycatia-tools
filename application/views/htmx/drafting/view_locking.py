from flask import request

from application import app
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

    r = view_locker(lock, inc_main_view, inc_background_view)

    if r:
        message = 'Views Unlocked!'
        if lock:
            message = 'Views Locked!'

        return f'<p class="alert alert-success">{message}</p>'
    else:
        return '<p class="alert alert-warning">The was a problem.</p>'
