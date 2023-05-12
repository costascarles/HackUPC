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


#Clase lobby que realmente es la partida, contiene jugadores y un chat
class Lobby:
    def __init__(self):
        self.jugadores = []
        self.chat = []
        
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        
    def enviar_mensaje(self, mensaje):
        self.chat.append(mensaje)
        
    def mostrar_chat(self):
        print("Chat:")
        for mensaje in self.chat:
            print(mensaje)

#Clase para la partida que contendrá un lobby y una serie de frases para el juego
class Partida:
    def __init__(self, lobby):
        self.lobby = lobby
        self.frases = []
        
    def agregar_frase(self, frase):
        self.frases.append(frase)
        
    def mostrar_frases(self):
        for frase in self.frases:
            print(frase)
