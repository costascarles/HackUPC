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
    "Me encantaría visitar {} algún día",
    "No puedo esperar para conocer {}",
    "El próximo destino en mi lista de viajes es {}",
    "{} es un lugar hermoso para visitar",
    "¿Alguien ha estado en {} antes?",
    "Nunca he estado en {} antes, ¡pero quiero ir!",
    "{} está en mi lista de deseos de viaje"
]

cursor.executemany('INSERT INTO frases (frase) VALUES (?)', [(frase,) for frase in frases])

conexion.commit()

conexion.close()
