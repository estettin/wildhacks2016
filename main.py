from flask import Flask, send_file
import requests
from predict import get_tags

app = Flask(__name__)




# mbp = open('apple.jpg', 'r')

@app.route("/")
def main():
    return "Hello World!"




@app.route("/fuckoff")
def fuckoff():
    return str(get_tags('mbp.jpg'))
    # print model.predict_by_filename('mbp.jpg')
    # r = requests.get("http://foaas.com/bucket/sebastian")
    # return send_file(mbp, mimetype='image/jpeg')
    # return send_file('apple.jpg')
    # return r.text
    # return "success"
    # return mbp.read()

if __name__ == "__main__":
    app.run()
