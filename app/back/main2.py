import sqlite3
import random
from flask import Flask, jsonify, request
from Jugador import Jugador
from Lobby import Lobby
from Mensaje import Mensaje
from Partida import Partida
from Game import Game
import time

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
    mensajes_completo.append(tupla[1].format(nombre_destino))
    print(tupla[1].format(nombre_destino))



while True:
    # Pedimos al usuario que ingrese el número de jugadores que quiere crear
    num_jugadores = int(input("Enter the number of players to create: "))

    # Creamos una lista vacía para almacenar los objetos de la clase Jugador
    jugadores = []

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
        print(jugador.nombre)

    bPartidaFinalizada = False
    bExisteJugadores = True

    #Comenzamos el bucle para la partida con las rondas que tendrá
    #Partida

    while bPartidaFinalizada == False and bExisteJugadores == True:
        #Ronda
        
        #Asignamos uno de los jugadores creados como el dibujante
        jugador_aleatorio = random.choice(jugadores)
        jugador_aleatorio.activarDibujante()
        
        #Este jugador es el dibujante en esta ronda
        print("Le toca dibujar a: " + jugador_aleatorio.nombre)    
        
        #Desactivamos el dibujante para los otros jugadores
        for jugador in jugadores:
            if(jugador.nombre != jugador_aleatorio.nombre):
                jugador.desactivarDibujante()
        
        mensajeDibujante = input("Mensaje a completar del dibujante: ")
        
        #fraseAleatoria = random.choice(mensajes_completo)
        lobby = Lobby(jugadores,mensajeDibujante)
        
        #Empezamos el timer
        inicio = time.time()
        
        bTiempoFinalizado = False
        bRespuestaCorrecta = False
        
        while bTiempoFinalizado == False and bRespuestaCorrecta == False: 
            
            tiempo_transcurrido = time.time() - inicio
            #print(tiempo_transcurrido)
            if(tiempo_transcurrido >= 30):
                bTiempoFinalizado = True
                    
            mensajeUser = "Hola"
            
            
            jugadorMensaje = jugadores[1]
            
            mensaje = Mensaje(jugadorMensaje, mensajeUser)            
            
            bRespuestaCorrecta = lobby.enviar_mensaje(mensaje,jugadorMensaje, tiempo_transcurrido)
            print(bRespuestaCorrecta)
            time.sleep(3)
            
            
            
    


    
    
    
    
    
    
    
    
    