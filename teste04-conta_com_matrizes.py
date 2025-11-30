matriz_2=[]
matriz_1=[]
resul_soma=[]

def SomaQuadrado():
    for i in range(2):
        for j in range(2):
            b= int(input(f"digite o item {j+1} da linha {i+1} : "))
            matriz_1.append(b)

    for i in range(2):
        for j in range(2):
            b= int(input(f"digite o item {j+1} da linha {i+1} : "))
            matriz_2.append(b)
    
    # Somar
    for i in range(2):
        linha = []
        for j in range(2):
            soma = matriz_1[i*2 + j] + matriz_2[i*2 + j] #que coisa ridicula
            linha.append(soma)
        resul_soma.append(linha)

    for row in resul_soma:
        print(row)
SomaQuadrado()