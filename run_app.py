from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue',interpreter = nlu_interpreter)

# https://api.slack.com/apps/AASPDV196/oauth?
input_channel = SlackInput('OAuth Access Token','Bot User OAuth Access Token',
'Verification Token',True)

agent.handle_channel(HttpInputChannel(5004,'/',input_channel))
