from .aicontent import openAIQuery

from flask import request
from flask_restx import Api, Resource, fields, Namespace

import jwt

from .config import BaseConfig

rest_api = Namespace('openai', description='OpenAI related operations')

import logging

logging.basicConfig(level='DEBUG')
logging.info("HERE 7")


cold_email_model = rest_api.model('ColdEmailModel', {
    'submission': fields.String(required=True, description='The user submission')
})

@rest_api.route('/cold-emails')
class ColdEmails(Resource):
    
    @rest_api.expect(cold_email_model, validate=True)
    def post(self):
        req_data = request.get_json()
        submission = req_data.get("submission")
        logging.info('cold emails called...{}'.format(submission))
        query = "Write a cold email to potential clients about: {}".format(submission)
        openAIAnswerUnformatted = openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        return {'result': openAIAnswer},200;