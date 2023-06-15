# Un sistema de control de acceso utiliza una base de datos para registrar las entradas y salidas de diferentes personas registradas.
# La base de datos tiene la siguiente estructura:
# * Tabla "Users": Contiene los campos "idUser", name, lastName, idJob.
# * Tabla "Jobs": Contiene los campos "idJob", "name".
# * Tabla "AccessLogs": Definir para no repetir información. Debera registrar la fecha y hora del acceso de una persona e indicar si entro o salio.

# * Cargar la base con informacion aleatoria.
# * Escribir la sentencia SQL que permita listar todos los usuarios que posee el sistema, con todos sus datos junto con el nombre del puesto que ocupan.
# * Listar las fechas de las ultimas 5 entradas de los gerentes, junto con el nombre y apellido de los mismos.

import sqlite3
import random
import datetime

conn = sqlite3.connect('baseDeDatos2.db')
print("Opened database successfully")

c=conn

# Crear tabla "Users"
conn.execute('''CREATE TABLE Users
            (idUser INT PRIMARY KEY     NOT NULL,
            name           TEXT    NOT NULL,
            lastName            TEXT     NOT NULL,
            idJob        INT);''')
print("Table created successfully")

# Crear tabla "Jobs"
conn.execute('''CREATE TABLE Jobs
            (idJob INT PRIMARY KEY     NOT NULL,
            name           TEXT    NOT NULL);''')
print("Table created successfully")

# Crear tabla "AccessLogs"
conn.execute('''CREATE TABLE AccessLogs
            (idAccessLog INT PRIMARY KEY     NOT NULL,
            idUser           INT    NOT NULL,
            date            TEXT     NOT NULL,
            time            TEXT     NOT NULL,
            type            TEXT     NOT NULL,
            FOREIGN KEY(idUser) REFERENCES Users(idUser));''')
print("Table created successfully")

# Cargar tabla "Jobs"
c.execute("INSERT INTO Jobs (idJob,name) \
        VALUES (1, 'Gerente')");
c.execute("INSERT INTO Jobs (idJob,name) \
        VALUES (2, 'Operario')");
c.execute("INSERT INTO Jobs (idJob,name) \
        VALUES (3, 'Administrativo')");
c.execute("INSERT INTO Jobs (idJob,name) \
        VALUES (4, 'Seguridad')");
c.execute("INSERT INTO Jobs (idJob,name) \
        VALUES (5, 'Mantenimiento')");
c.execute("INSERT INTO Jobs (idJob,name) \
        VALUES (6, 'Limpieza')");

# Cargar tabla "Users"
todos_users=[]
for i in range(1,101):
    name = random.choice(['Juan','Pedro','Maria','Jose','Ana','Lucia','Diego','Julieta','Sofia','Miguel'])
    lastName = random.choice(['Perez','Gomez','Rodriguez','Fernandez','Gonzalez','Lopez','Diaz','Martinez','Sanchez','Gimenez'])
    idJob = random.randint(1,6)
    todos_users.append((i,name,lastName,idJob))
c.executemany("INSERT INTO Users (idUser,name,lastName,idJob) \
        VALUES (?,?,?,?)", todos_users);

# Cargar tabla "AccessLogs"
todos_accessLogs=[]
for i in range(1,1001):
    idUser = random.randint(1,100)
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")
    type = random.choice(['Entrada','Salida'])
    todos_accessLogs.append((i,idUser,date,time,type))
c.executemany("INSERT INTO AccessLogs (idAccessLog,idUser,date,time,type) \
        VALUES (?,?,?,?,?)", todos_accessLogs);

conn.commit()
print("Records created successfully")

# Listar todos los usuarios
cursor = conn.execute("SELECT Users.idUser, Users.name, Users.lastName, Jobs.name from Users INNER JOIN Jobs ON Users.idJob = Jobs.idJob")
for row in cursor:
    print("ID = ", row[0])
    print("NOMBRE = ", row[1])
    print("APELLIDO = ", row[2])
    print("CARGO = ", row[3], "\n")

# Listar las fechas de las ultimas 5 entradas de los gerentes, junto con el nombre y apellido de los mismos.
cursor = conn.execute("SELECT Users.name, Users.lastName, AccessLogs.date from Users INNER JOIN AccessLogs ON Users.idUser = AccessLogs.idUser WHERE Users.idJob = 1 AND AccessLogs.type = 'Entrada' ORDER BY AccessLogs.date DESC LIMIT 5")
for row in cursor:
    print("NOMBRE = ", row[0])
    print("APELLIDO = ", row[1])
    print("FECHA = ", row[2], "\n")

print("Operation done successfully")
conn.close()

