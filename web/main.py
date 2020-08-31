import os

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def web():
    #name = os.environ.get('NAME', 'foXCat')
    #return 'Hello {}!'.format(name)
	return render_template('Andy.html')
	
@app.route('/Andy')
def andy():	
	return render_template('Andy.html')
	
@app.route('/index')
def index():	
	return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))