#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return "<h1> Hello World </h1>"

@app.route('/home/<word>/', methods=['GET', 'POST'])
def home(word):
	if request.method == 'GET':
		print(request.headers)
	return render_template('sample.html', wordList=['hello', 'this', 'is', 'sample']);



# Handles the file upload and returns the response by analyzing the file.
@app.route('/upload/', methods=['POST'])
def upload_file():
	try:
		uploaded_file = request.files['file']
		if uploaded_file.filename != '':
			for line in uploaded_file:
				print(line);
			return "Success";
			# TODO Add the code for responding the webpage with the result generated by AI algorithm.
			# 		Data should be in the following format
			# 		{
			#			aiVsHuman: { ai: x, human: y },
			#			imagesBlured: { blured: x, unBlured: y },
			#			...
			#			...
			#		} 
	except Error:
		return "Error";


app.run('localhost', 5000);