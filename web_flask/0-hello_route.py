#!/usr/bin/python3
"""the script starts a flask app
	the application listens to 0.0.0. port 5000
"""
from flask import FLask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
	"this route function say hello HBNB"
	return("Hello HBNB")

if __name__== __main__:
	app.run(host="0.0.0.0")
