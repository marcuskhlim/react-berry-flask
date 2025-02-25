# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import json

from flask import Flask
from flask_cors import CORS

from .routes import rest_api as ns1
from .openai import rest_api as ns2
from .models import db
from flask_restx import Api

app = Flask(__name__)

app.config.from_object('api.config.BaseConfig')

db.init_app(app)

rest_api = Api(version="1.0", title="API")
rest_api.add_namespace(ns1, path='/api/users')
rest_api.add_namespace(ns2, path='/api/openai')
rest_api.init_app(app)
CORS(app)

# Setup database
@app.before_first_request
def initialize_database():
    db.create_all()

"""
   Custom responses
"""

@app.after_request
def after_request(response):
    """
       Sends back a custom error with {"success", "msg"} format
    """

    if int(response.status_code) >= 400:
        response_data = json.loads(response.get_data())
        if "errors" in response_data:
            response_data = {"success": False,
                             "msg": list(response_data["errors"].items())[0][1]}
            response.set_data(json.dumps(response_data))
        response.headers.add('Content-Type', 'application/json')
    return response
