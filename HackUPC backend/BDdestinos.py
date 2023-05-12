import sqlite3

#Creamos la conexión a la base de datos con los destinos
conexion = sqlite3.connect('destinos.db')

#
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Destinos (
        nombre TEXT,
        pais TEXT,
        continente TEXT,
        precio INTEGER
    )
''')

conexion.commit()
