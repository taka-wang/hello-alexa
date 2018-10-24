from flask import Flask
from flask_ask import Ask, question, session, statement

app = Flask(__name__)
ask = Ask(app, "/")

@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

@ask.launch
def start_skill():
    msg = 'Hello there, would you like to know the inwin?'
    return question(msg)

@ask.intent("YesIntent")
def yes_intent():
    msg = 'Contemporary & Innovative defines the InWin brand. It reflects in the appearance and features of our products. With an artistic approach in mind, InWin products integrate technology, functionality, user-friendly, safety, practicality and overall quality, providing an entirely new experience with each product.'
    return statement(msg)

@ask.intent("NoIntent")
def no_intent():
    msg = 'I am not sure why you asked me to run then, but okay... bye'
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)
