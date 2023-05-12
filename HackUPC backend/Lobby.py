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
