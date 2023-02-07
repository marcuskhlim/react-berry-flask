# -*- encoding: utf-8 -*-

"""
Copyright (c) 2019 - present AppSeed.us
"""

from api import app, db
import logging
'''
if __name__ != '__main__':
    gunicorn_error_handlers = logging.getLogger('gunicorn.error').handlers
    app.logger.handlers.extend(gunicorn_error_handlers )
    app.logger.addHandler(myhandler1)
    app.logger.addHandler(myhandler2)
    app.logger.info('my info')
    app.logger.debug('debug message')
'''

@app.shell_context_processor
def make_shell_context():
    return {"app": app,
            "db": db
            }

logging.basicConfig(level='DEBUG')
logging.info("LOG SOMETHING")


@app.route('/')
def default_route():
    """Default route"""
    app.logger.debug('this is a DEBUG message')
    app.logger.info('this is an INFO message')
    app.logger.warning('this is a WARNING message')
    app.logger.error('this is an ERROR message')
    app.logger.critical('this is a CRITICAL message')
    return jsonify('hello world')

if __name__ == '__main__':
    app.logger.info('FLASK APP starting...')
    app.run(debug=True, host="0.0.0.0")
