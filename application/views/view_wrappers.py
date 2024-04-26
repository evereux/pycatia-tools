from functools import wraps

from flask import abort

from application.pycatia_scripts.com_objects import get_app_object


def catia_v5_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not get_app_object():
            return abort(500, 'Could not access COM object. Is CATIA V5 running?')
        return func(*args, **kwargs)
    return wrapper
