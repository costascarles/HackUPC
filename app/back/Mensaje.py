class Mensaje:
    def __init__(self, jugador, contenido):
        self.autor = jugador
        self.contenido = contenido
        
    def __str__(self):
        return f"{self.autor}: {self.contenido}"

