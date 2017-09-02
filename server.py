
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',  methods=['GET', 'POST'])
def search():
    return "Search %s" % request.form.get ('txt','Def value' )