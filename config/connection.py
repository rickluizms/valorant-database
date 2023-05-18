import mysql.connector

# Configuração da conexão
mydb = {
    'user': 'root',
    'password': 'Lz.157675',
    'host': 'localhost',
    'database': 'valorant_dba',
    'raise_on_warnings': True
}

mydb2 = {
    'user': 'root',
    'password': 'Lz.157675',
    'host': 'localhost',
    'database': 'world_stats',
    'raise_on_warnings': True
}

connection = mysql.connector.connect(**mydb)

connection2 = mysql.connector.connect(**mydb2)

