from twilio.rest import Client

# Your Twilio credentials
ACCOUNT_SID = "AC81c069b8462d854ff980df2fc5c4dc96"
AUTH_TOKEN = "e41db4c3a346847ae29d17efedd55aab"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms(message):
    client.messages.create(
        body=message,
        from_="+17625338668",
        to="+919019269504"
    )

# Test message
send_sms("🚨 Animal detected in Zone A. it is a wild animal" )