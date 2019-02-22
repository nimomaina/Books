import os
class Config:
    '''
    General configuration parent class
    '''
    GOODREADS_API_BASE_URL = "https://www.googleapis.com/books/v1/volumes?q={}"
    GOODREADS_API_KEY ="God's Work"


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}