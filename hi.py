from flask import flask

app = flask (_name_)

@app.route("/")
def hello_world():
	return "<b>Hi world</b>"

@app.route("/hi")
def hello_world():
	return "<b>Hi world</b>"