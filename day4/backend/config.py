class Config():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///day4.sqlite3'
    API_PREFIX = '/api'

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    SECRET_KEY = 'shhhhh....... very secret'
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'