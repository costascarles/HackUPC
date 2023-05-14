import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('destinos.db')

# Crear un cursor
cursor = conexion.cursor()

# Realizar la consulta SELECT
cursor.execute('SELECT * FROM Destinos')

# Obtener los resultados
resultados = cursor.fetchall()

# Mostrar los resultados
for resultado in resultados:
    print(resultado)

# Cerrar la conexión
conexion.close()

