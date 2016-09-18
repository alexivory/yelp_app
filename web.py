from flask import Flask, render_template, request
import yelp_api
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
app = Flask(__name__)



@app.route("/")
def index():
	location = request.values.get('location')
	term = None
	businesses = None
	# term = None
	# location = None
	# yelpy = None
	# if address:
	# 	yelpy = yelp_api.get_businesses(term, address)
	if location:
		businesses = yelp_api.get_businesses(location, term)
	return render_template('index.html', businesses=businesses)

@app.route("/about")
def about():
	return render_template('about.html')
	
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)