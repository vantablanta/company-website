from distutils.debug import DEBUG


class Config:
    """Parent class"""

class ProdConfig(Config):
    """Production Confugartins"""

class DevConfig(Config):
    """"Developement Configurationstions"""
    DEBUG = True