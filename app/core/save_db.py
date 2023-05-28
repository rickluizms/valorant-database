import pandas as pd
import pyodbc

class Database():

    def __init__(self):
        self.inject

    def inject(dataframe, sql, table_name):
        
        # Configuração da conexão
        server = sql.server  # Nome ou endereço IP do servidor SQL Server
        db = sql.database  # Nome do banco de dados
        conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={db};Trusted_Connection=yes;'
        
        try:
            # Conectando ao banco de dados
            connection = pyodbc.connect(conn_str)
            
            if connection:
                print('Conexão estabelecida!')
                
                # Cria um cursor para executar consultas
                cursor = connection.cursor()
                
                # Verifica se a tabela existe
                cursor.execute(f"IF OBJECT_ID('{table_name}', 'U') IS NOT NULL DROP TABLE {table_name}")
                
                # Cria uma nova tabela com o mesmo nome
                cursor.execute(f"CREATE TABLE {table_name} (id INT IDENTITY(1,1) PRIMARY KEY)")
                
                columns = list(dataframe.columns)
                
                for column in columns:
                    # Adiciona as colunas na tabela
                    cursor.execute(f"ALTER TABLE {table_name} ADD {column} VARCHAR(255)")
                
                for _, row in dataframe.iterrows():
                    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['?']*len(columns))})"
                    values = tuple(row[column] for column in columns)
                    cursor.execute(query, values)
                
                connection.commit()
                print('DADOS ATUALIZADOS COM SUCESSO!')
                cursor.close()
                connection.close()
                print('Conexão encerrada!')
        
        except pyodbc.Error as error:
            print(f'Erro ao conectar ao SQL Server: {error}')