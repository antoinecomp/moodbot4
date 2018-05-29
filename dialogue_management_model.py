from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

# keep track of things happening if need of debugging
logger = logging.getLogger(__name__)

# training the final model
def train_dialogue(domain_file = 'mood_domain.yml',
					model_path = './models/dialogue',
					training_data_file = './data/stories.md'):

	agent = Agent(domain_file,policies = [MemoizationPolicy(),KerasPolicy()])
	
	agent.train(training_data_file,
				# max_history = 3, not supported anymore
				epochs=300,
				batch_size = 50,
				validation_split = 0.2,
				augmentation_factor = 50)

	agent.persist(model_path)
	# return the final dialogue agent
	return agent

def run_weather_bot(serve_forever =True):
	interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu/test')
	#load an agent
	agent= Agent.load('./models/dialogue',interpreter = interpreter)

	# we can read the messages
	if serve_forever:
		agent.handle_channel(ConsoleInputChannel())

	return agent

if __name__ == '__main__':
	train_dialogue()
	run_weather_bot()
