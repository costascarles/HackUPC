class Mensaje:
    def __init__(self, autor, contenido):
        self.autor = autor
        self.contenido = contenido
        
    def __str__(self):
        return f"{self.autor}: {self.contenido}"

