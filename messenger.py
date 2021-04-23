import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

def send_message(data):

    msg = f"New Cases: {data[0]} \nNew Deaths: {data[1]} \n% of Population with at least one dose: {data[2]} \n% of Population Fully Vaccinated: {data[3]}"

    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                        body=msg,
                        from_='+16107569568',
                        to='+16312359493'
                    )