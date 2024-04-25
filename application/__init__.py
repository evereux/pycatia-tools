from dotenv import load_dotenv
import os

from flask import Flask


load_dotenv('.env')
app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['WTF_CSRF_SECRET_KEY'] = os.getenv('WTF_CSRF_SECRET_KEY')
app.config['SERVER_NAME'] = os.getenv('SERVER_NAME')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024

from application.jinja2.menu import render_menu
from application.version import version

app.jinja_env.globals.update(version=version)
app.jinja_env.globals.update(version=version)
app.jinja_env.globals.update(render_menu=render_menu)

from application import views
