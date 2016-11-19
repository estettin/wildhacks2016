from twilio.rest import TwilioRestClient

ACCOUNT_SID = "ACe266ac010d75136677ddb422c88fd5cb" 
AUTH_TOKEN = "357024b143141688264d414ce75447fe" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
source = "+12242654689"

message = client.messages.create(to="+15515790231", from_=source,
                                 body="Hello there!")
 
