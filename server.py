
from flask import Flask
from flask import request
from flask import render_template
from database import db_session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',  methods=['GET', 'POST'])
def search():
    return "Search %s" % request.form.get ('txt','Def value' )

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()