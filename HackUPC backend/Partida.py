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
            
