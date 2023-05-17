import mysql.connector

def save_dataframe(connection, dataframe, table_name):

        try:

            if connection.is_connected():

                print('Conexão estabelecida!')

                # Cria um cursor para executar consultas
                cursor = connection.cursor()

                # Obtém o nome das colunas do dataframe
                columns = list(dataframe.columns)

                for _, row in dataframe.iterrows():

                    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(columns))})"
                    values = tuple(row[column] for column in columns)
                    cursor.execute(query, values)

                connection.commit()

                cursor.close()
                
        except mysql.connector.Error as error:
            print(f'Erro ao conectar ao MySQL: {error}')

def close_connection(connection):
    connection.close()
    print('Conexão encerrada!')

def update_dataframe(connection, dataframe, table_name):

        try:

            if connection.is_connected():

                print('Conexão estabelecida!')

                # Cria um cursor para executar consultas
                cursor = connection.cursor()

                # Obtém o nome das colunas do dataframe
                columns = list(dataframe.columns)

                delete_query = f"DELETE FROM {table_name}"
                cursor.execute(delete_query)

                for _, row in dataframe.iterrows():

                    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(columns))})"
                    values = tuple(row[column] for column in columns)
                    cursor.execute(query, values)

                connection.commit()

                cursor.close()
                
        except mysql.connector.Error as error:
            print(f'Erro ao conectar ao MySQL: {error}')

def close_connection(connection):
    connection.close()
    print('Conexão encerrada!')