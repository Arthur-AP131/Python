import teste07_database as db

print("\n [1] select all \n [2] select all where preço < 10\n")

z = int(input(""))

a = ""

if z == 1:

    a = "SELECT * FROM fruta"

    b=db.query(a)

    for row in b:
        print(f'id:',row['id'], 'fruta:',row['nome'],'preço:',row['preço'])
elif z == 2:

    a="SELECT * FROM fruta WHERE preço < 10"

    b=db.query(a)

    for row in b:
        print(f'id:',row['id'], 'fruta:',row['nome'],'preço:',row['preço'])

