import requests
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from create_model import *

app = Flask(__name__)


def get_state(text):
    if is_concern(text):
        return True
    return False


@app.route('/sms', methods=['GET', 'POST'])
def sms():
    input_message = request.values.get('Body').lower()  # gets incoming message
    bot_response = MessagingResponse()
    state = get_state(input_message)

    if state:  # based on incoming message, send different message
        bot_response.message('There is a potential mental health concern.')
    else:
        bot_response.message('Good to go!')

    return str(bot_response)


if __name__ == '__main__':
    app.run(debug=True)