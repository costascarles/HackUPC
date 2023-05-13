#Clase lobby que realmente es la partida, contiene jugadores y un chat
class Lobby:
    def __init__(self,jugador):
        self.jugadores = [jugador]
        self.chat = []
        self.existePartida = True
        
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        
    def eliminar_jugador(self, jugador):
        self.jugadores.remove(jugador)
        if(range(self.jugadores) == 0) : 
            self.existePartida = False
        
    def enviar_mensaje(self, mensaje):
        self.chat.append(mensaje)
        
    def mostrar_chat(self):
        print("Chat:")
        for mensaje in self.chat:
            print(mensaje)
