import config
from app import app


debug = True
if config.PRODUCTION is True:
    debug = False
app.run(debug=debug)
