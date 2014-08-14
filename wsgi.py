import os
os.environ['APP_CONFIG'] = '/var/www/test.provserv/application.cfg'
from app import app

app = Flask(__name__)
app.config.from_object('app.default_config')
app.config.from_envvar('APP_CONFIG')
