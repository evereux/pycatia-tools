from flask import render_template, request, url_for, redirect

from application import app
from application.forms.forms import FormDocumentSave
from application.pycatia_scripts.common import get_documents, save_documents


def is_it_true(value):
    return value.lower() == 'true'


@app.route('/documents', methods=['GET', 'POST'])
def documents():
    sort_key = request.args.get('sort_key')
    reverse = request.args.get('reverse', default=False, type=is_it_true)

    documents = get_documents(sort_key=sort_key, reverse=reverse)
    form = FormDocumentSave(documents=documents)

    if form.validate_on_submit():
        save_documents(form)
        return redirect(url_for('documents'))

    return render_template('documents.html', documents=documents, form=form)
