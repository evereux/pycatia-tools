from application import app
from application.support.template import render_template
from application.views.view_wrappers import catia_v5_required
from application.pycatia_scripts.settings import parameters


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
    return render_template(
        'drafting_save_as.html',
    )


@app.route('/drafting/insert_template')
@catia_v5_required
def drafting_insert_template():
    return render_template(
        'drafting_template.html',
        parameters=parameters
    )
