from flask import Flask, request, redirect
import twilio.twiml
import ScavengerHunt

app = Flask(__name__)
global game = None
@app.route("/", methods = ['GET', 'POST'])
def initialize():
	from_number = request.values.get('From', None)
	msg_body = request.values.get('Body', None).split('\n')
	if msg_body[0] == 'Create'
		createGame(from_number, msg_body[1], msg_body[2:])

	return ""



if __name__ == "__main__":
	app.run(debug=False)