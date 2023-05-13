import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('frases.db')

# Crear un cursor
cursor = conexion.cursor()

# Realizar la consulta SELECT
cursor.execute('SELECT * FROM Frases')

# Obtener los resultados
resultados = cursor.fetchall()

# Mostrar los resultados
for resultado in resultados:
    print(resultado)

# Cerrar la conexión
conexion.close()

palabra = "Paris"

for tupla in resultados:
    mensaje_completo = tupla[1].format(palabra)
    print(mensaje_completo)