import openai
from .config import BaseConfig
openai.api_key = BaseConfig.OPENAI_API_KEY

import logging
logging.basicConfig(level='DEBUG')

def openAIQuery(query):
	response = openai.Completion.create(
		engine="davinci-instruct-beta-v3",
		prompt=query,
		temperature=0.7,
		max_tokens=200,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0)

	if 'choices' in response:
		if len(response['choices']) > 0:
			answer = response['choices'][0]['text']
		else:
			answer = 'Opps sorry, you beat the AI this time'
	else:
		answer = 'Opps sorry, you beat the AI this time'
	return answer
