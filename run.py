from flask import Flask, request, redirect, session
import twilio.twiml


SECRET_KEY = '357024b143141688264d414ce75447fe'

app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!
callers = {
    "+15515790231": "Elana",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    image_url = request.values.get('MediaUrl0', None)

    resp = twilio.twiml.Response()
    resp.message(image_url)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)