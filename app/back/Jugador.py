#Clase que contiene un Jugador con nombre y puntuación
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntuacion = 0
        self.dibujar = False
        
    def sumar_puntos(self, puntos):
        self.puntuacion += puntos
        
    def restar_puntos(self, puntos):
        self.puntuacion -= puntos
    
    def mostrar_puntuaciones(jugadores):
        print("Puntuaciones:")
        for jugador in jugadores:
            print(f"{jugador.nombre}: {jugador.puntuacion}")
            
    def activarDibujante(self):
        self.dibujar = True
        
    def desactivarDibujante(self): 
        self.dibujar = False
    def to_dict(self):
        return {'nombre': self.nombre, 'puntuacion': self.puntuacion,'dibujar':self.dibujar}
