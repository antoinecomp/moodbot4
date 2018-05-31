# moodbot4

Welcome abroad ! This moodbot was based on the work of Justina Petraitite ! We hope you will enjoy it

## How does it work 

Basically, its pretty simple.

### You want to test it on your own ?

Great ! That's a good start. You have to create an account on apixu.com to have the weather services. You will therefore have to grant him the api key in `actions.py`. Then you may run `̀python dialogue_management_model.py`. It will give you an interactive test on the command line where you will be able to talk with you chatbot.

### You want to test it with Slack ?

Yeah ! Let's make our relationship looks official.
First you must have to create a Slack workspace. Then to create a bot, give him a name, grant him the Auth & Permissions tokes in `run_app.py` and the 

## You want to modify it ?

### The domain ?

Of course. To create your own bot mind universe you may modify `mood_domain.yml`. You may modify the intents he may recognize from your sentences, the entities he may get from them you provide and the actions he takes from the decision his machine learning algorithm learned him.

### The machine learning algorithm ?

Soon.

## Virtual Environnments are great !

We had to virtualenv from version control, the rest of you will have to recreate the virtualenv when they want to work on the project. For that we have versioned the requirements.txt file with the dependencies.

And then you, if you do not have the virtualenv directory, would have to create it and install the dependencies (for example with venv):

python3 -m venv "MoodEnv"
source MoodEnv / bin / activate
pip install -r requirements.txt

And repeat the pip install every time a dependency is added to the project.
