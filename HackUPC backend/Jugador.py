#Clase que contiene un Jugador con nombre y puntuación
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntuacion = 0
        
    def sumar_puntos(self, puntos):
        self.puntuacion += puntos
        
    def restar_puntos(self, puntos):
        self.puntuacion -= puntos
    
    def mostrar_puntuaciones(jugadores):
        print("Puntuaciones:")
        for jugador in jugadores:
            print(f"{jugador.nombre}: {jugador.puntuacion}")

