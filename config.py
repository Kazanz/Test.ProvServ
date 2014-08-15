class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    DEBUG = True

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://test@127.0.0.1/hivelocity_shared'

class ProdConfig(Config):
    # TODO make sure this connect to the production database
    SQLALCHEMY_DATABASE_URI = 'mysql://hivelocity:PASSWORD@hvdb1-private/myvelocity'
    DEBUG = False
