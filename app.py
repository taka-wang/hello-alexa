import logging
import os
from flask import Flask, json, render_template
from flask_ask import Ask, question, session, statement

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@app.route('/')
def homepage():
    return "Hi there, how ya doin?"


@ask.launch
def launch():
    card_title = render_template('card_title')
    question_text = render_template('welcome')
    reprompt_text = render_template('welcome_reprompt')
    return question(question_text).reprompt(reprompt_text).simple_card(card_title, question_text)



@ask.launch
def launch():
    msg = 'Hello there, would you like to know the InWin?'
    msg2 = "I didn't get that. Whould you like to know the brand philosophy of InWin"
    msg = "Hello there, I am your assistant, What's your name?"
    msg2 = "mmm, Can you tell me your name?"
    card_title = render_template('card_title')
    question_text = render_template('welcome')
    reprompt_text = render_template('welcome_reprompt')
    return question(question_text).reprompt(reprompt_text).simple_card(card_title, question_text)

@ask.launch
def launch():
    card_title = render_template('card_title')
    question_text = render_template('welcome')
    reprompt_text = render_template('welcome_reprompt')
    return question(question_text).reprompt(reprompt_text).simple_card(card_title, question_text)

@ask.intent("introductionIntent",  mapping={'username': 'username'})
def introduction_intent():
    session.attributes["username"] = username
    card_title = render_template('card_title')
    question_text = render_template('introduction', username=username)
    reprompt_text = render_template('introduction_reprompt', username=username)
    return question(question_text).reprompt(reprompt_text).simple_card(card_title, question_text)

@ask.intent("YesIntent")
def yes_intent():
    msg = 'Contemporary & Innovative defines the InWin brand. It reflects in the appearance and features of our products. With an artistic approach in mind, InWin products integrate technology, functionality, user-friendly, safety, practicality and overall quality, providing an entirely new experience with each product.'
    return statement(msg).simple_card('Brand Philosophy', msg)

@ask.intent("NoIntent")
def no_intent():
    username = session.attributes.get("username")
    bye_text = render_template('bye', username=username)
    return statement(bye_text).simple_card('Bye', msg)

@ask.intent("ConnectIntent", mapping={'serialno': 'serialno'})
def connect_intent(serialno):
    msg = 'Ok, I will connect you echo to {} {} {} {}'.format(
        serialno[0], serialno[1], serialno[2], serialno[3])
    return statement(msg).simple_card('Connect', msg)

@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can ask me to tell you the brand philosophy of InWin, would you like to know the InWin now?'
    return question(speech_text).reprompt(speech_text).simple_card('Help', speech_text)

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    app.run(debug=True)
