#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import json

from models import model_ai_human

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html');


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

			ai_human_score = model_ai_human.calculate_ai_vs_human_score(text)

			analysis_data = { 'ai_vs_human': ai_human_score }

			return render_template('output.html', ai = ai_human_score['ai'], human = ai_human_score['human']);

	except KeyError or TypeError:
		return "<h4> Failed to retrieve the information </h4>";

app.run('localhost', 5000);
