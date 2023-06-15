import sqlite3
conn = sqlite3.connect('baseDeDatos.db')
print("Opened database successfully")

c=conn

# Crear tabla "Users"
conn.execute('''CREATE TABLE estudiantes
            (idEstudiante INT PRIMARY KEY     NOT NULL,
            nombre           TEXT    NOT NULL,
            apellido            TEXT     NOT NULL,
            edad        INT);''')
print("Table created successfully")

c.execute("INSERT INTO estudiantes (idEstudiante,nombre,apellido,edad) \
        VALUES (1, 'Juan', 'Perez', 20 )");

c.execute("INSERT INTO estudiantes (idEstudiante,nombre,apellido,edad) \
        VALUES (2, 'Maria', 'Gomez', 21 )");

todos_estudiantes=[
    (3, 'Pedro', 'Gonzalez', 22),
    (4, 'Jose', 'Rodriguez', 23),
    (5, 'Ana', 'Fernandez', 24),
]

c.executemany("INSERT INTO estudiantes (idEstudiante,nombre,apellido,edad) \
        VALUES (?,?,?,?)", todos_estudiantes);
    
conn.commit()
print("Records created successfully")

cursor = conn.execute("SELECT idEstudiante, nombre, apellido, edad from estudiantes")
for row in cursor:
    print("ID = ", row[0])
    print("NOMBRE = ", row[1])
    print("APELLIDO = ", row[2])
    print("EDAD = ", row[3], "\n")

print("Operation done successfully")
conn.close()
