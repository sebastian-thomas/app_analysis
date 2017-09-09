import sys
from flask import Flask
from flask import request
from flask import render_template
from database import init_db, db_session
from flask_socketio import SocketIO
from flask_socketio import send, emit

from fetch_data import getKeywords

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretseb'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('search_event') 
def search(data):
    print(data["term"], file=sys.stderr)
    emit('log', {"msg":"Got search term " + data["term"]})
    getKeywords (socketio, data["term"])

@app.route('/search',  methods=['GET', 'POST'])
def search():
    return "Search %s" % request.form.get ('txt','Def value' )

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()
    socketio.run(app)