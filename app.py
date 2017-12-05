#!python3
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

	return render_template('index.html')

app.run()	