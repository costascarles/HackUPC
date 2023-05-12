import sqlite3

#Creamos la conexión a la base de datos con los destinos
conexion = sqlite3.connect('destinos.db')

#Crea una conexión a la base de datos SQLite utilizando la función connect de sqlite3. 
# Si la base de datos no existe, se creará automáticamente.
cursor = conexion.cursor()

#Crea una tabla en la base de datos para almacenar los destinos. 
# En este ejemplo, la tabla se llamará Destinos y tendrá cuatro columnas: nombre, pais, continente.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Destinos (
        nombre TEXT PRIMARY KEY,
        pais TEXT,
        continente TEXT
    )
''')

conexion.commit()

#Inserta los destinos en la tabla utilizando la sentencia INSERT INTO.
destinos = [
    ('Tokyo', 'Japan', 'Asia'),
    ('Kyoto', 'Japan', 'Asia'),
    ('Sapporo', 'Japan', 'Asia'),
    ('Seoul', 'South Korea', 'Asia'),
    ('Bangkok', 'Thailand', 'Asia'),
    ('Singapore', 'Singapore', 'Asia'),
    ('Kuala Lumpur', 'Malaysia', 'Asia'),
    ('Bali', 'Indonesia', 'Asia'),
    ('Sydney', 'Australia', 'Oceania'),
    ('Melbourne', 'Australia', 'Oceania'),
    ('Auckland', 'New Zealand', 'Oceania'),
    ('Queenstown', 'New Zealand', 'Oceania'),
    ('Paris', 'France', 'Europe'),
    ('Barcelona', 'Spain', 'Europe'),
    ('London', 'United Kingdom', 'Europe'),
    ('Amsterdam', 'Netherlands', 'Europe'),
    ('Rome', 'Italy', 'Europe'),
    ('New York', 'United States', 'North America'),
    ('San Francisco', 'United States', 'North America'),
    ('Toronto', 'Canada', 'North America'),
    ('Mexico City', 'Mexico', 'North America'),
    ('Santiago de Chile', 'Chile', 'South America'),
    ('Buenos Aires', 'Argentina', 'South America'),
    ('Rio de Janeiro', 'Brazil', 'South America'),
    ('Lima', 'Peru', 'South America'),
    ('New Delhi', 'India', 'Asia'),
    ('Mumbai', 'India', 'Asia'),
    ('Shanghai', 'China', 'Asia'),
    ('Beijing', 'China', 'Asia'),
    ('Dubai', 'United Arab Emirates', 'Asia'),
    ('Istanbul', 'Turkey', 'Asia/Europe'),
    ('Moscow', 'Russia', 'Europe'),
    ('Prague', 'Czech Republic', 'Europe'),
    ('Vienna', 'Austria', 'Europe'),
    ('Zurich', 'Switzerland', 'Europe'),
    ('Oslo', 'Norway', 'Europe'),
    ('Stockholm', 'Sweden', 'Europe'),
    ('Copenhagen', 'Denmark', 'Europe'),
    ('Helsinki', 'Finland', 'Europe'),
    ('Warsaw', 'Poland', 'Europe'),
    ('Budapest', 'Hungary', 'Europe'),
    ('Dublin', 'Ireland', 'Europe'),
    ('Edinburgh', 'United Kingdom', 'Europe'),
    ('Glasgow', 'United Kingdom', 'Europe'),
    ('Brussels', 'Belgium', 'Europe'),
    ('Berlin', 'Germany', 'Europe'),
    ('Hamburg', 'Germany', 'Europe'),
    ('Munich', 'Germany', 'Europe'),
    ('Rotterdam', 'Netherlands', 'Europe'),
    ('Lisbon', 'Portugal', 'Europe'),
    ('Madrid', 'Spain', 'Europe'),
    ('Valencia', 'Spain', 'Europe'),
    ('Seville', 'Spain', 'Europe'),
    ('Malaga', 'Spain', 'Europe'),
    ('Bilbao', 'Spain', 'Europe'),
    ('Milan', 'Italy', 'Europe'),
    ('Florence', 'Italy', 'Europe'),
    ('Venice', 'Italy', 'Europe'),
    ('Naples', 'Italy', 'Europe'),
    ('Bratislava', 'Slovakia', 'Europe'),
    ('Bucharest', 'Romania', 'Europe'),
    ('Athens', 'Greece', 'Europe'),
    ('Sofia', 'Bulgaria', 'Europe'),
    ('Cairo', 'Egypt', 'Africa'),
    ('Casablanca', 'Morocco', 'Africa'),
    ('Cape Town', 'South Africa', 'Africa'),
    ('Johannesburg', 'South Africa', 'Africa'),
    ('Nairobi', 'Kenya', 'Africa'),
    ('Tunis', 'Tunisia', 'Africa'),
    ('Dar es Salaam', 'Tanzania', 'Africa'),
    ('Abidjan', 'Ivory Coast', 'Africa'),
    ('Lagos', 'Nigeria', 'Africa'),
    ('Dakar', 'Senegal', 'Africa'),
    ('Marrakech', 'Morocco', 'Africa'),
    ('Zanzibar', 'Tanzania', 'Africa'),
    ('Accra', 'Ghana', 'Africa'),
    ('Addis Ababa', 'Ethiopia', 'Africa'),
    ('Vatican City', 'Vatican City', 'Europe'),
    ('The Hague', 'Netherlands', 'Europe'),
    ('Krakow', 'Poland', 'Europe'),
    ('Vilnius', 'Lithuania', 'Europe'),
    ('Riga', 'Latvia', 'Europe'),
    ('Tallinn', 'Estonia', 'Europe'),
    ('Toulouse', 'France', 'Europe'),
    ('Brno', 'Czech Republic', 'Europe'),
    ('Salzburg', 'Austria', 'Europe'),
    ('Bath', 'United Kingdom', 'Europe'),
    ('Inverness', 'United Kingdom', 'Europe'),
    ('Galway', 'Ireland', 'Europe'),
    ('Saint Petersburg', 'Russia', 'Europe/Asia'),
    ('Vladivostok', 'Russia', 'Asia'),
    ('Jakarta', 'Indonesia', 'Asia'),
    ('Phuket', 'Thailand', 'Asia'),
    ('Siem Reap', 'Cambodia', 'Asia'),
    ('Colombo', 'Sri Lanka', 'Asia'),
    ('Male', 'Maldives', 'Asia'),
    ('Jerusalem', 'Israel', 'Asia'),
    ('Petra', 'Jordan', 'Asia'),
    ('Beirut', 'Lebanon', 'Asia'),
    ('Antalya', 'Turkey', 'Asia/Europe')
]

cursor.executemany('INSERT INTO Destinos VALUES (?, ?, ?)', destinos)

conexion.commit()

conexion.close()
