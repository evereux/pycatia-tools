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

from application.version import version
from application import views

app.jinja_env.globals.update(version=version)
