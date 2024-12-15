import flask
from flask import request
from flask import render_template
from flask import abort
from flask.logging import default_handler
import flask_sqlalchemy
from logging.config import dictConfig
import logging
import sys


app = flask.Flask(__name__)

gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)
app.logger.removeHandler(default_handler)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format':'[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s',
        'datefmt':'%Y-%m-%d %H:%M:%S %z',
    }},
    'handlers': {
        'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
        },
        'file': {
        'class': 'logging.FileHandler',
        'filename': 'app.log',  # The file where logs will be stored
        'formatter': 'default',
        },
    },
    'loggers':{
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi','file']
        }
    }
})

@app.route('/')
def index():
    return render_template('index.ejs',request=request.headers  )

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)