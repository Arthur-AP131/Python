import mysql.connector
from mysql.connector import Error

def conectar(): # função pra estabelecer conexão com o banco
    try:
        MyDB = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="frutasDB"
        )

        if MyDB.is_connected(): # se tiver conectado retorna a conexão
            return MyDB
        else: #se não so exibe que a conexão não funcionou
            print("Erro na conexão!!")

    except mysql.connector.Error as err: # se tiver algum erro quando ele tenta conectar exibe o erro
        print(f'Erro: {err}')
        return None # impede de retonar a conexão


def query(sql,param = None): 
       
        conn = conectar()# coloca a conexão em uam variavel pra facilitar
        if conn is None: # se não tiver conexão não retorna nada
           return[]
       
        try:
            cursor = conn.cursor(dictionary=True) # cria o cursor e faz com que o resultado da query venha um pouco melhor
            cursor.execute(sql, param or ()) # pega os parametros da função e executam eles no banco
            resultado = cursor.fetchall() # pega o resultado e coloca em uma variavel
            return resultado # retorna o resultado

        except Error as err: # se tiver erro ele manda que erro que foi e impede de rotornar alguma coisa
            print(f"Erro na query: {err}")
            return []

        finally: # quando termina fecha tudo
            cursor.close()
            conn.close()




    