from twilio.rest import Client
from flask import Flask, Response

# ================= TWILIO CREDENTIALS =================
ACCOUNT_SID = "ACCSID"
AUTH_TOKEN = "AUTHID"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# ================= PHONE NUMBERS =================
FROM_NUMBER = "+17625338668"
TO_NUMBER = "+91********"

# 🔴 Replace with your ngrok URL
PUBLIC_URL = "https://carlish-uncataloged-herlinda.ngrok-free.dev"

# ================= FLASK APP =================
app = Flask(__name__)

# ================= MAKE CALL =================
def make_call():
    call = client.calls.create(
        to=TO_NUMBER,
        from_=FROM_NUMBER,
        url=f"{PUBLIC_URL}/voice"
    )
    print("Call SID:", call.sid)

# ================= KANNADA VOICE RESPONSE =================
@app.route("/voice", methods=['GET', 'POST'])
def voice():
    twiml_response = """
    <Response>
        <Say voice="alice" language="kn-IN">
            ಎಚ್ಚರಿಕೆ! ನಿಮ್ಮ ಜಮೀನಿನಲ್ಲಿ ಪ್ರಾಣಿಯನ್ನು ಪತ್ತೆಹಚ್ಚಲಾಗಿದೆ. ದಯವಿಟ್ಟು ತಕ್ಷಣ ಕ್ರಮ ಕೈಗೊಳ್ಳಿ.
        </Say>
    </Response>
    """
    return Response(twiml_response, mimetype='text/xml')

# ================= TRIGGER ENDPOINT =================
@app.route("/trigger", methods=['GET'])
def trigger():
    make_call()
    return "Call triggered successfully!"

# ================= RUN SERVER =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)