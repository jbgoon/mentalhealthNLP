from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from alecc_responses import Alecc

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    # Get recent text from user
    body = request.values.get('Body', None)
    bot = Alecc(body)
    message = bot.response()

    # Start our TwiML response
    # Then add a message
    resp = MessagingResponse()
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, render_template
# from dotenv import load_dotenv
# from utils import fetch_sms
#
# # loads .env variables containing twilio sid and auth token
# load_dotenv()
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     sms = fetch_sms() # fetches sms texts
#     return render_template("index.html", sms=sms)
