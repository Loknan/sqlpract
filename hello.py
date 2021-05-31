from flask import Flask
from flask import render_template

app = Flask (__name__)

@app.route("/")
def helloworld():
	return "<p>Hello world</p>"

	@app.route("/hi")
def hiworld():
	return "<b>Hi world</b>"