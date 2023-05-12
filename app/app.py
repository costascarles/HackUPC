from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

players = {}

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def handleMessage(msg):
    print("Message: "+msg)
"""
return render_template('/index.html')
@app.route('/game')
def game():
    return render_template('game.html')


@socketio.on('connect')
def on_connect():
    player_id = request.sid
    players[player_id] = {'symbol': ''}
    emit('player_id', player_id)

@socketio.on('disconnect')
def on_disconnect():
    player_id = request.sid
    if player_id in players:
        del players[player_id]

"""
if __name__=='__main__':
    socketio.run(app, host='0.0.0.0')