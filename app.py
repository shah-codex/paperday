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
