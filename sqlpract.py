from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
Bookstore = Flask (__name__)

@Bookstore.route("/")
def home():
	return "<p>new page</p>"

@Bookstore.route("/about")
def about():
	return render_template ('opening.html')
