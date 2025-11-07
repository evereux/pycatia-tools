from flask import request, render_template

from application import app
from application.views.url_prefixes import htmx
from application.pycatia_scripts.drafting.save_drawing import save_as_dxf
from application.pycatia_scripts.drafting.save_drawing import save_as_pdf


@app.route(f'{htmx}/drafting/save_as_pdf', methods=['POST'])
def htmx_drafting_save_as_pdf():
    exclude = request.form.get('exclude_sheet') or None
    target_directory = request.form.get('target_directory') or None

    output = save_as_pdf(exclude_sheets=exclude, target_directory=target_directory)
    data = output['data']
    errors = output['errors']

    if errors:
        return render_template('partials/errors.html', errors=errors)

    if data:
        return render_template('partials/success.html', data=data)

    return render_template('partials/error.html')


@app.route(f'{htmx}/drafting/save_as_dxf', methods=['POST'])
def htmx_drafting_save_as_dxf():
    include = request.form.get('include_sheet') or None
    target_directory = request.form.get('target_directory') or None

    output = save_as_dxf(include_sheets=include, target_directory=target_directory)
    data = output['data']
    errors = output['errors']

    if errors:
        return render_template('partials/errors.html', errors=errors)

    if data:
        return render_template('partials/success.html', data=data)

    return render_template('partials/error.html')
