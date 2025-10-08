class Config():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///day2.sqlite3'
    RESTFUL_PREFIX = '/api'

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'