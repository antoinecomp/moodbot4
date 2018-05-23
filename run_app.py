from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu/test')
agent = Agent.load('./models/dialogue',interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-368538464663-368538465959-369270903815-61394ddb86d62dd8cd0fd90830c33e3e','xoxb-368538464663-367528130096-Qn2Ph7DrjqICYSCqwzQrXUGv','Y7P8mPpixzZUD4tllVUPuKuf',True)

agent.handle_channel(HttpInputChannel(5004,'/',input_channel))
