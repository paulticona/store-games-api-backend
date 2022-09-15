from distutils.command.config import config
from os import getenv
from datetime import timedelta


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = getenv('JWT_SECRET')
    JWT_ACCESS_TOKEN = timedelta(hours=1)
    JWT_REFRESH_TOKEN = timedelta(hours=3)


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


config_env = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
