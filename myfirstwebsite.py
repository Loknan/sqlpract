from flask import Flask

app = Flask (__name__)

@app.route("/")
def helloworld():
	return "<p>my first website</p>"

@app.route("/serve")
def hiworld():
	return "<b>services</b>"

@app.route("/about")
def hiworld():
	return "<b>services</b>"