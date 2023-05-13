class Game:
    def __init__(self,partida):
        self.partidas = [partida]
        self.existePartida = True
        
    def agregar_partida(self, partida):
        self.partidas.append(partida)
        
    def remover_partida(self, partida):
        self.partidas.remove(partida)
        if(range(self.partidas) == 0): 
            self.existePartida = False
        
    def listar_partidas(self):
        for partida in self.partidas:
            print(partida)
