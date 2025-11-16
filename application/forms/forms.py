from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, SubmitField, StringField, Form, BooleanField
from wtforms.validators import Optional


class _FormDocumentSave(Form):
    filename = StringField(
        'filename',
        validators=[Optional()],
        render_kw={
            'class': 'form-control form-control-sm p-1',
            'readonly': True,
        }
    )
    path = StringField(
        'path',
        validators=[Optional()],
        render_kw={
            'class': 'form-control form-control-sm',
            'readonly': True,
        }
    )
    saved = StringField(
        'saved',
        validators=[],
        render_kw={
            'class': 'form-control form-control-sm text-center',
            'readonly': True,
        }
    )
    save = BooleanField(
        'save',
        validators=[Optional()],
        render_kw={
            'class': 'form-check-input',
        }
    )


class FormDocumentSave(FlaskForm):
    documents = FieldList(
        FormField(_FormDocumentSave),
        min_entries=1,
    )
    save = SubmitField(
        'Save',
        render_kw={
            'class': 'btn btn-primary btn-sm rounded-0'
        },
    )
