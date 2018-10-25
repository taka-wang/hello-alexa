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

@ask.intent("IntroductionIntent",  mapping={'username': 'username'})
def introduction_intent(username):
    session.attributes["username"] = username
    card_title = render_template('card_title')
    question_text = render_template('introduction', username=username)
    reprompt_text = render_template('introduction_reprompt', username=username)
    return question(question_text).reprompt(reprompt_text).simple_card(card_title, question_text)

@ask.intent("YesIntent")
def yes_intent():
    yes_text = render_template('philosophy')
    return statement(yes_text).simple_card('Brand Philosophy', yes_text)

@ask.intent("NoIntent")
def no_intent(username):
    username = session.attributes.get("username")
    card_title = render_template('card_title')
    bye_text = render_template('bye', username=username)
    return statement(bye_text).simple_card(card_title, bye_text)

@ask.intent("ConnectIntent", mapping={'serialno': 'serialno'})
def connect_intent(serialno):
    card_title = render_template('card_title')
    connect_text = render_template('connect', a=serialno[0], b=serialno[1], c=serialno[2], d=serialno[3])
    return statement(connect_text).simple_card(card_title, connect_text)

@ask.intent('AMAZON.HelpIntent')
def help():
    card_title = render_template('card_title')
    help_text = render_template('help')
    return question(help_text).reprompt(help_text).simple_card(card_title, help_text)

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    app.run(debug=True)
