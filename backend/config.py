import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = True
    HOST = os.environ.get('BACKEND_HOST')
    PORT = os.environ.get('BACKEND_PORT')
    SQLALCHEMY_DATABASE_URI = "postgresql://{0}:{1}@{2}:{3}/{4}".format(os.environ.get("POSTGRES_USER"),
                                                                        os.environ.get("POSTGRES_PASSWORD"),
                                                                        os.environ.get("POSTGRES_HOST"),
                                                                        os.environ.get("POSTGRES_PORT"),
                                                                        os.environ.get("POSTGRES_DB")
                                                                        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class ProductionConfig(BaseConfig):
    DEBUG = False
