import sqlite3
import random
from Jugador import Jugador
from Lobby import Lobby
from Mensaje import Mensaje
from Partida import Partida
from flask import Flask, jsonify, request
from Game import Game

app = Flask(__name__)

#Creamos el array con los destinos 
# Conectar a la base de datos de destinos
conexion = sqlite3.connect('destinos.db')

# Crear un cursor
cursor = conexion.cursor()

# Definimos el nombre del destino que queremos buscar
nombre_destino = 'Tokyo'

# Ejecutamos la consulta con un WHERE para buscar el destino por nombre
cursor.execute('SELECT * FROM Destinos WHERE nombre=?', (nombre_destino,))

# Obtener los resultados
resultados = cursor.fetchall()

# Mostrar los resultados
for resultado in resultados:
    print(resultado)

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
    mensajes_completo.append(tupla[1].format(nombre_destino))
    print(tupla[1].format(nombre_destino))

# Pedimos al usuario que ingrese el número de jugadores que quiere crear
num_jugadores = int(input("Ingrese el número de jugadores a crear: "))

# Creamos una lista vacía para almacenar los objetos de la clase Jugador
jugadores = []

#Creamos el lobby
lobby = Lobby()

# Iteramos la cantidad de veces que se especificó para crear un jugador en cada iteración
for i in range(num_jugadores):
    # Pedimos al usuario que ingrese el nombre del jugador
    nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
    # Creamos un objeto de la clase Jugador con el nombre ingresado
    jugador = Jugador(nombre)
    # Agregamos el objeto a la lista de jugadores
    jugadores.append(jugador)

# Mostramos los nombres de los jugadores creados
print("Jugadores creados:")
for jugador in jugadores:
    lobby.agregar_jugador(jugador)
    print(jugador.nombre)
    
jugador_aleatorio = random.choice(jugadores)
jugador_aleatorio.activarDibujante()
print(jugador_aleatorio.nombre)

for jugador in jugadores:
    if(jugador.nombre != jugador_aleatorio.nombre):
        jugador.desactivarDibujante()
        

#Control de los mensajes
# Endpoint para solicitudes GET
#@app.route('/saludo', methods=['GET'])
#def saludar():
    #mensaje = request.args.get('mensaje')  # Obtenemos el valor del parámetro "nombre"
    
mensaje = Mensaje("Eric", "texto")

lobby.enviar_mensaje(mensaje)

#Creamos la partida
partida = Partida(lobby)

for mensaje in mensajes_completo:
    partida.agregar_frase(mensaje)
    
 
game = Game(partida) 
#game.agregar_partida(partida)
#Falta hacer comprobaciones para cuando no haya partida, eliminar el game.   
partida2 = Partida(lobby)
game.agregar_partida(partida2)


    
    
    
    
    
    
    
    
    