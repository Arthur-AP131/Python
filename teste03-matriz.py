n_coluna = int(input("qual o tamanho x?: "))
n_linha = int(input("qual o tamanho y?: "))

matriz=[]

for i in range(n_coluna):
    linha=[]
    for j in range(n_linha):
        b= int(input(f"digite o item {j+1} da linha {i+1} : "))
        linha.append(b)
    matriz.append(linha)

for row in matriz:
    print(row)