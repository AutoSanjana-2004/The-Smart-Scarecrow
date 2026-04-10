from flask import Flask, request, Response
from twilio.rest import Client

app = Flask(__name__)

# Twilio credentials
ACCOUNT_SID = "YOUR_SID"
AUTH_TOKEN = "YOUR_AUTH_TOKEN"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# 📲 SMS Alert
@app.route('/alert', methods=['GET'])
def alert():
    zone = request.args.get('zone')

    message = f"Animal detected in Zone {zone}"

    client.messages.create(
        body=message,
        from_="+17625338668",
        to="+919019269504"
    )

    return "SMS Sent!"


# 📞 Voice Call Trigger
@app.route('/make_call', methods=['GET'])
def make_call():
    call = client.calls.create(
        to="+919019269504",
        from_="+17625338668",
        url="https://carlish-uncataloged-herlinda.ngrok-free.dev"
    )
    return "Calling..."


# 🎧 TwiML (plays your audio)
@app.route('/call', methods=['GET'])
def call():
    twiml = """
    <Response>
        <Play>https://drive.google.com/uc?export=download&amp;id=1-76PWSnGOgTs8XMvuLUClIFTMBFoV9Pc</Play>
    </Response>
    """
    return Response(twiml, mimetype='text/xml')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)