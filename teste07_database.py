import mysql.connector

try:
    MyDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="frutasDB"
    )

    if MyDB.is_connected:
        print("Conexão bem sucedida!!")
    else:
        print("Erro na conexão!!")

    cur = MyDB.cursor()

    cur.execute("SELECT * FROM fruta WHERE preço < 10 ")

    for row in cur.fetchall():
        print(row)

    MyDB.close()
    
except mysql.connector.Error as err:
    print(f'Erro: {err}')



    
