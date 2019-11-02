# views.py


from flask import render_template, request
from app import app
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
from pymongo import MongoClient

import urllib
import location

client = Client('TWILIO_ACCOUNT_SID', 'TWILIO_AUTH_TOKEN')
dbClient = MongoClient('mongodb+srv://dbAdmin:hackrpiadmin@cluster0-abtsj.mongodb.net/test?retryWrites=true&w=majority')
db = dbClient.data

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/sms', methods=['POST'])
def inbound_sms():
    response = MessagingResponse()
    response.message('Thanks for texting! Please wait for a local weather alert')

    # Grab the zip code from the body of the text message.
    zip_code = urllib.parse.quote(request.form['Body'])

    # Grab the relevant phone numbers.
    from_number = request.form['From']
    to_number = request.form['To']

    userData = {
        "number": from_number,
        "zipcode": zip_code
    }

    db.insert_one(userData)

    message = client.messages.create(
        body = location.get_weather_alert(zip_code),
        from_ = from_number, 
        to = to_number
    )


    return str(response)


# A route to handle the logic for phone calls.
@app.route('/call', methods=['POST'])
def outbound_sms():
    zip_code = request.args.get('zipcode')

    response = MessagingResponse()
    response.message(location.get_weather_alert(zip_code))
    return str(response)