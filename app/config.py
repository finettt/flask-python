import os

class Config(object):
    USER = os.environ.get('POSTGRES_USER','finett')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD','sandr44666')
    HOST = os.environ.get('POSTGRES_HOST','127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT','5532')
    DB = os.environ.get('POSTGRES_DB','mydb')
    
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = 'dasfghj76253vgsafd827356ugdw76235'
    SQLALCHEMY_TRACK_MODIFICATIONS = True