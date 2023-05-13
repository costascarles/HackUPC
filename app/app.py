from flask import Flask, render_template, send_from_directory, request,jsonify
from flask_socketio import SocketIO, send
from flask_cors import CORS
import back.Partida as p
import back.Lobby
import back.Jugador as j
import sqlite3
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app,static_folder='build')
""""app.debug = True"""
CORS(app)
partidas=[]
players = {}

@app.route('/')
def index():
    """return send_from_directory(app.static_folder, 'index.html')"""
    return render_template("index.html", flask_token="Hello   world")

@app.route('/connect', methods=['POST'])
def connect():
    username = request.json['username']
    room = request.json['room']
    isCreated= False
    for i in partidas:
        if i.idRoom == room:
            jugador_añadir = j.Jugador(username)
            i.agregar_player(jugador_añadir)
            isCreated=True
    
    if isCreated == False:
        if len(partidas)==0:
            partidas.append(p.Partida(0,j.Jugador(username),"Frase"))
        else:
            partidas.append(p.Partida(len(partidas)+1,j.Jugador(username),"Frase"))
    
    return jsonify([{'status': "success", 'info': "User Added"}])
    
@app.route('/room/<int:room_id>', methods=['GET'])
def get_room(room_id):
     jugadores = []
     for i in partidas:
        if i.idRoom == room_id:            
            jugadores=i.players
     serialized_jugadores = [jugador.to_dict() for jugador in jugadores]
     # Aquí iría la lógica para obtener la información de la sala con el ID especificado
     return jsonify({'room_id': room_id, 'players': serialized_jugadores})

@app.route('/rooms', methods=['GET'])
def get_all_rooms():
    # Aquí iría la lógica para obtener todas las salas
    # por ejemplo, se puede obtener todas las salas de una base de datos usando SQLAlchemy:
    rooms_list = []
    for i in partidas:
        rooms_list.append({'id':i.idRoom,'numPlayers':i.numPlayers})

    return jsonify(rooms_list)

@socketio.on('message')
def handleMessage(msg):
    print("Message: "+msg)

if __name__=='__main__':
    socketio.run(app, host='0.0.0.0')
    rooms = [{'id': '1', 'numPlayers': '0'},{'id': '2', 'numPlayers': '0'},{'id': '3', 'numPlayers': '0'},{'id': '4', 'numPlayers': '0'}]
    