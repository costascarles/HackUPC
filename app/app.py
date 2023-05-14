import random
from flask import Flask, render_template, send_from_directory, request,jsonify,make_response
from flask_socketio import SocketIO, send
from flask_cors import CORS
import back.Partida as p
import back.Lobby
import back.Jugador as j
import back.Mensaje as m
import sqlite3
import base64
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app,static_folder='build')
""""app.debug = True CORS(app)"""
app.config['CORS_ALLOWED_ORIGINS'] = ['*.example.com', '*.example.org', '*.example.net', '*.png']
CORS(app, resources={r"/*": {"origins": "*"}})

partidas=[]
players = {}

@app.route('/')
def index():
    """return send_from_directory(app.static_folder, 'index.html')"""
    return render_template("index.html", flask_token="")

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
            partidas.append(p.Partida(0,j.Jugador(username),getFrase()))
        else:
            partidas.append(p.Partida(len(partidas),j.Jugador(username),getFrase()))
    
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

@app.route('/room/<int:room_id>/missatges', methods=['POST'])
def set_roomMsg(room_id):
     mensajes = request.json['msg']
     player= request.json['player']
     for i in partidas:
        if i.idRoom == room_id:            
            i.msgs.append(m.Mensaje(player,mensajes))
     
     # Aquí iría la lógica para obtener la información de la sala con el ID especificado
     return jsonify([{'status': "success", 'info': "Message Added"}])

@app.route('/room/<int:room_id>/missatges', methods=['GET'])
def get_roomMsg(room_id):
     mensajes = []
     for i in partidas:
        if i.idRoom == room_id:            
            mensajes=i.msgs
     serialized_mensajes = [{"player": m.autor,"msg": m.contenido}for m in mensajes]
     # Aquí iría la lógica para obtener la información de la sala con el ID especificado
     return jsonify({'room_id': room_id, 'mensajes': serialized_mensajes})

@app.route('/rooms', methods=['GET'])
def get_all_rooms():
    # Aquí iría la lógica para obtener todas las salas
    # por ejemplo, se puede obtener todas las salas de una base de datos usando SQLAlchemy:
    rooms_list = []
    for i in partidas:
        rooms_list.append({'id':i.idRoom,'numPlayers':i.numPlayers})

    return jsonify(rooms_list)

@app.route('/room/<int:room_id>/selectDrawer', methods=['POST'])
def set_round(room_id):   
    for i in partidas:
        if i.idRoom == room_id:
            dibujante=i.select_drawer()    
    return jsonify({"status":"success" ,"info": "Player Selected" })

@app.route('/room/<int:room_id>/fixFrase', methods=['POST'])
def set_FraseRound(room_id):   
    text = request.json['text']
    for i in partidas:
        if i.idRoom == room_id:
            sentence=i.complete_sentence(text)    
    return jsonify({"status":"success" ,"info": "Round Started" })

@app.route('/room/<int:room_id>/check', methods=['POST'])
def check_round(room_id): 
    mensajes = request.json['msg']
    player= request.json['player']  
    for i in partidas:
        if i.idRoom == room_id:
            win,winer=i.check_status(mensajes,player)    
    return jsonify({"status":"success" , "result": win, "winer": player })

@app.route('/room/<int:room_id>/frase', methods=['GET'])
def get_frase(room_id): 
    for i in partidas:
        print(i)
        if i.idRoom == room_id:
            sent= i.winFrase    
    return jsonify({"status":"success" , "frase": sent })

@app.route('/room/<int:room_id>/getImg', methods=['GET'])
def get_image(room_id):
    with open('image.png', 'rb') as f:
        image = f.read()
    response = make_response(image)
    response.headers.set('Content-Type', 'image/png')
    return response

@app.route('/room/<int:room_id>/postImg', methods=['POST'])
def upload_image(room_id):
    image_data = request.form.get('image_data')
    if image_data:
        image_data = image_data.split(",")[1]
        with open("image.png", "wb") as f:
            f.write(base64.b64decode(image_data))
        return "Imagen recibida correctamente."
    else:
        return "No se recibió ninguna imagen."

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png'}


@socketio.on('message')
def handleMessage(msg):
    print("Message: "+msg)

def getFrase():
    #Creamos el array con los destinos 
    # Conectar a la base de datos de destinos
    conexion = sqlite3.connect('destinos.db')

    # Crear un cursor
    cursor = conexion.cursor()

    # Definimos el nombre del destino que queremos buscar
    #nombre_destino = city

    # Ejecutamos la consulta con un WHERE para buscar el destino por nombre
    cursor.execute('SELECT * FROM Destinos ')

    # Obtener los resultados
    ALLresultados = cursor.fetchall()
    city = random.choice(ALLresultados)[0]
    # Mostrar los resultados
    #for resultado in resultados:
    #   print(resultado)

    # Cerrar la conexión
    conexion.close()


    #Conectar a la base de datos de frases
    conexion = sqlite3.connect('frases.db')

    # Crear un cursor
    cursor = conexion.cursor()

    # Realizar la consulta SELECT
    cursor.execute('SELECT * FROM Frases')

    # Obtener los resultados
    resultados = cursor.fetchall()

    # Mostrar los resultados
    #for resultado in resultados:
        #print(resultado)

    # Cerrar la conexión
    conexion.close()

    mensajes_completo = []

    for tupla in resultados:
        mensajes_completo.append(tupla[1].format(city))
        print(tupla[1].format(city))
    return mensajes_completo
if __name__=='__main__':
    socketio.run(app, host='0.0.0.0')
    rooms = [{'id': '1', 'numPlayers': '0'},{'id': '2', 'numPlayers': '0'},{'id': '3', 'numPlayers': '0'},{'id': '4', 'numPlayers': '0'}]
    