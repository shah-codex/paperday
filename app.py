#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

from models import model_ai_human

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return "<center> <h1> Paperday </h1> </center>"


# Handles the file upload and returns the response by analyzing the file.
@app.route('/upload/', methods=['POST'])
def upload_file():
	try:
		uploaded_file = request.files['file']

		# Conversion of the file to pure text based format.
		if uploaded_file.filename != '':
			text = "";
			for line in uploaded_file:
				text += line.decode('utf-8')

			
			# TODO [Future Feature]
			# Convert the data taken from word document to text (string) format.
			# 		Data should be in the following format
			# 		{
			#			aiVsHuman: { ai: x, human: y },
			#			imagesBlured: { blured: x, unBlured: y },
			#			...
			#			...
			#		}

			ai_human_score = model_ai_human.calculate_ai_vs_human_score(text)

			analysis_data = { 'ai_vs_human': ai_human_score }

			return render_template('sample.html', wordList = list(analysis_data['ai_vs_human'].values()));

	except KeyError or TypeError:
		return "<h4> Failed to retrieve the information </h4>";

app.run('localhost', 5000);
