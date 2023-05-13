#Clase lobby que realmente es la partida, contiene jugadores y un chat
class Lobby:
    def __init__(self, jugadores, frase):
        self.jugadores = jugadores
        self.chat = []
        self.fraseLobby = frase
        
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        
    def eliminar_jugador(self, jugador):
        self.jugadores.remove(jugador)
        if(range(self.jugadores) == 0) : 
            self.existePartida = False
        
    def enviar_mensaje(self, mensaje, jugador, tiempo):
        self.chat.append(mensaje)
        puntos = 60 - tiempo
        
        if(puntos < 10):
            puntos = 10
            
        if(mensaje.contenido==self.fraseLobby):
            jugador.sumar_puntos(puntos)
            return True
        else:
            return False

    def cambiaFrase(self,fraseNueva):
        self.fraseLobby = fraseNueva
        
    def mostrar_chat(self):
        print("Chat:")
        for mensaje in self.chat:
            print(mensaje)
            
    def limpiarChat(self):
        self.chat = []
