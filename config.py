class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql://b2ceb3df30624a:83483118@us-cdbr-east-05.cleardb.net/heroku_16eddd733c1d435?reconnect=true"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 300
    SECRET_KEY = "horrible_secret_key"
    LOGIN_DISABLED = True