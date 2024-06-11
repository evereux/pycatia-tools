from pathlib import Path

from application import app
from application.support.template import render_template
from application.views.view_wrappers import catia_v5_required
from application.pycatia_scripts.settings import drawing_template
from application.pycatia_scripts.settings import json_data
from application.pycatia_scripts.the_document import PTDrawingDocument


@app.route('/drafting')
@catia_v5_required
def drafting():
    return render_template(
        'drafting.html',
    )


@app.route('/drafting/views')
@catia_v5_required
def drafting_views():
    return render_template(
        'drafting_views.html',
    )


@app.route('/drafting/save_as')
@catia_v5_required
def drafting_save_as():
    exclude_sheets = ', '.join(json_data['drafting']['pdf']['exclude_sheets'])
    return render_template(
        'drafting_save_as.html',
        exclude_sheets=exclude_sheets,
    )

@app.route('/drafting/save_as/pdf')
@catia_v5_required
def drafting_save_as_pdf():
    exclude_sheets = ', '.join(json_data['drafting']['pdf']['exclude_sheets'])
    return render_template(
        'drafting_save_as_pdf.html',
        exclude_sheets=exclude_sheets,
    )

@app.route('/drafting/save_as/dxf')
@catia_v5_required
def drafting_save_as_dxf():
    include_sheets = ', '.join(json_data['drafting']['dxf']['include_sheets'])
    return render_template(
        'drafting_save_as_dxf.html',
        include_sheets=include_sheets,
    )


@app.route('/drafting/insert_template')
@catia_v5_required
def drafting_insert_template():
    return render_template(
        'drafting_template.html',
        parameters=drawing_template['parameters']
    )
