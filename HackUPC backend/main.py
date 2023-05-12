from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

board = np.zeros((3, 3))
players = {}

@app.route('/')
def index():
    return render_template('index.html')

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

@socketio.on('move')
def on_move(data):
    player_id = request.sid
    row = data['row']
    col = data['col']
    symbol = players[player_id]['symbol']
    
    # Actualiza el tablero con el movimiento del jugador
    board[row][col] = symbol
    
    # Verifica si hay un ganador
    winner = check_winner(board)
    
    # Envía la actualización del tablero y el ganador a todos los jugadores
    emit('update_board', board.tolist(), broadcast=True)
    if winner:
        emit('game_over', winner, broadcast=True)
def check_winner(board):
    # Verifica las filas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
    
    # Verifica las columnas
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != 0:
            return board[0][j]
    
    # Verifica las diagonales
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    
    # Si no hay ganador
    return None
        
