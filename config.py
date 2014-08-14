PRODUCTION = False

if PRODUCTION:
    # TODO make sure this connect to the production database
    SQLALCHEMY_DATABASE_URI = 'mysql://hivelocity:PASSWORD@hvdb1-private/myvelocity'
else:
    SQLALCHEMY_DATABASE_URI = 'mysql://test@127.0.0.1/hivelocity_shared'

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
