from flask import request
from flask_restx import Api, Resource, fields, Namespace

import jwt

from .config import BaseConfig

rest_api = Namespace('openai', description='OpenAI related operations')

import logging

logging.basicConfig(level='DEBUG')
logging.info("HERE 2")


cat = rest_api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

CATS = [
    {'id': 'felix', 'name': 'Felix'},
]

@rest_api.route('/')
class CatList(Resource):
    @rest_api.doc('list_cats')
    @rest_api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return CATS