#Clase para la partida que contendrá un lobby y una serie de frases para el juego
import random
from datetime import datetime

class Partida:
    def __init__(self, room,player, frases):
        self.idRoom = room
        self.players = [player]
        self.frases = frases
        self.numPlayers = 1
        self.msgs= []
        self.timeStampStart = 0
        self.timeStampEnd = 0
        self.winFrase = ""
        
        
    def agregar_player(self, player):
        self.players.append(player)
        self.numPlayers+=1

    def eliminar_player(self, player):
        self.players.remove(player)
        self.numPlayers-=1
        
    def escoger_frase(self):
       frase = random.choice(self.frases)
       self.frases.remove(frase)
       
    def add_msg(self, ms):
        self.msgs.append(ms)

    def select_drawer(self):
        self.players
        player = random.choice(self.players)
        player.activarDibujante()
        self.winFrase = random.choice(self.frases)
        self.timeStampStart = datetime.timestamp(datetime.now())
        return player
    def complete_sentence(self, destino,extraText):              
        self.winFrase[1].format(destino)
        self.winFrase +=extraText
            
    def check_status(self,frase,player):
        win = False

        if frase == self.winFrase:
            self.timeStampEnd = datetime.timestamp(datetime.now())
            win = True
            for i in self.players:
                if i.nombre == player:
                    i.puntuacion+= ((len(self.players)-1)*0.05 + 1) - (self.timeStampEnd -self.timeStampStart)/100
                if i.dibujar == True:
                    i.desactivarDibujante()
        
        return win,player
    
    def to_dict(self):
        return {'room': self.idRoom, 'msg': self.msgs}
        
            
