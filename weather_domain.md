slots: <!--placeholders for the vaues that should help the bot to keep track of the context of the conversation-->
	location:
		type: text
	
intents:
 - greet
 - goodbye

entities:
 - location

templates: <!--text reponses that bot should send back to the user when specific action-->
	utter_great:
		- 'hello ! How can I help'
	utter_goodbye:
		- 'Talk to you later'
		- 'Bye bye :('
	utter_ask_location:
		- 'In what location'

actions:
 - utter_great
 - utter_goodbye
 - utter_ask_location
 - action.ActionWeather
