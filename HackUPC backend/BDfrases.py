import sqlite3

#Creamos la conexión a la base de datos con los destinos
conexion = sqlite3.connect('frases.db')

#Crea una conexión a la base de datos SQLite utilizando la función connect de sqlite3. 
# Si la base de datos no existe, se creará automáticamente.
cursor = conexion.cursor()

#Crea una tabla en la base de datos para almacenar los destinos. 
# En este ejemplo, la tabla se llamará Destinos y tendrá cuatro columnas: nombre, pais, continente.
cursor.execute('''CREATE TABLE IF NOT EXISTS frases
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  frase TEXT)''')

conexion.commit()

#Inserta los destinos en la tabla utilizando la sentencia INSERT INTO.
frases = [    
    "In {}, I'm going to ",
    "I can't wait to visit in {}",
    "I plan to spend my days in {}",
    "I'm excited to go in {}",
    "I want to go on a in {}",
    "I'm looking forward to trying in {}",
    "I would love to visit in {}",
    "I can't wait to see in {}",
]

cursor.executemany('INSERT INTO frases (frase) VALUES (?)', [(frase,) for frase in frases])

conexion.commit()

conexion.close()
