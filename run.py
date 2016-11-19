from flask import Flask, request, redirect, session
import twilio.twiml
import predict


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

	# image_url = "None"
	# if request.values.get('MediaUrl0'):
	# 	image_url = request.values.get('MediaUrl0')
	# 	resp = twilio.twiml.Response()
	# 	resp.message(image_url)
	return predict.get_tags("https://static.independent.co.uk/s3fs-public/thumbnails/image/2013/01/24/12/v2-cute-cat-picture.jpg")
	


if __name__ == "__main__":
	app.run(debug=True)