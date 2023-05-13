from flask import Flask, render_template, send_from_directory, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app,static_folder='build')

players = {}

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/connect', methods=['POST'])
def connect():
    username = request.json['username']
    room = request.json['room']
    isNewRoom = request.json['isNewRoom']

@app.route('/disconnect', methods=['DELETE'])
def disconnect():
    username = request.json['username']
    
@app.route('/room/<room_id>', methods=['GET'])
def get_room(room_id):
    # Aquí iría la lógica para obtener la información de la sala con el ID especificado
    return jsonify({'room_id': room_id, 'info': 'información de la sala'})
   
@socketio.on('message')
def handleMessage(msg):
    print("Message: "+msg)
"""
@app.route('/connect', methods=['POST'])
def connect():
    username = request.json['username']
    room = request.json['room']
    
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