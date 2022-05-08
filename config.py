import os

class Config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:29654387@localhost/watchlist_test'
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:29654387@localhost/watchlist'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}

# class Config(object):
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
# class DevelopmentConfig(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:wamzy@127.0.0.1:5432/charts'
#     SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'
#     JWT_SECRET_KEY = 'some-secret-key'
# class ProductionConfig():
#     SQLALCHEMY_DATABASE_URI = 'postgres://rftwdbhjfsozch:e52930939d3f2f7281ae4e35e6546de7ddcec230f6e1c129e07d8d600a718102@ec2-46-137-84-173.eu-west-1.compute.amazonaws.com:5432/d1ki50794ckm6l'
#     SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'