import logging
from flask import Flask
from flask_ask import Ask, question, session, statement

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

@ask.launch
def start_skill():
    msg = 'Hello there, would you like to know the InWin?'
    msg2 = "I didn't get that. Whould you like to know the brand philosophy of InWin"
    return question(msg).reprompt(msg2).simple_card('Ask Inwin', msg)

@ask.intent("YesIntent")
def yes_intent():
    msg = 'Contemporary & Innovative defines the InWin brand. It reflects in the appearance and features of our products. With an artistic approach in mind, InWin products integrate technology, functionality, user-friendly, safety, practicality and overall quality, providing an entirely new experience with each product.'
    return statement(msg).simple_card('Ask Inwin', msg)

@ask.intent("NoIntent")
def no_intent():
    msg = 'I am not sure why you asked me to run then, but okay... bye'
    return statement(msg).simple_card('Ask Inwin', msg)

@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can ask me to tell you the brand philosophy of InWin!'
    return question(speech_text).reprompt(speech_text).simple_card('Ask Inwin', speech_text)

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    app.run(debug=True)
