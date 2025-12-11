matriz_2=[]
matriz_1=[]
resultado=[]

def MontarMatriz(n_linhas,n_colunas):

    for i in range(n_linhas):
            for j in range(n_colunas):
                b= int(input(f"digite o item {j+1} da linha {i+1} : "))
                matriz_1.append(b)

    for i in range(n_linhas):
            for j in range(n_colunas):
                b= int(input(f"digite o item {j+1} da linha {i+1} : "))
                matriz_2.append(b)

def Adição(n_linhas,n_colunas):
    try: 

        MontarMatriz(n_linhas,n_colunas)
    
        # Somar
        for i in range(n_linhas):
            linha = []
            for j in range(n_colunas):
                soma = matriz_1[i*2 + j] + matriz_2[i*2 + j] #que coisa ridicula
                linha.append(soma)
            resultado.append(linha)

        for row in resultado:
            print(row)
    except:
        print("erro, tente novamente")
def Subtracao(n_linhas,n_colunas):
    try: 
        
        MontarMatriz(n_linhas,n_colunas)
    
        # subtrair
        for i in range(n_linhas):
            linha = []
            for j in range(n_colunas):
                subtracao = matriz_1[i*2 + j] - matriz_2[i*2 + j] #que coisa ridicula
                linha.append(subtracao)
            resultado.append(linha)

        for row in resultado:
            print(row)
    except:
        print("erro, tente novamente")
def Multiplicacao(n_linhas_1, n_colunas_1, n_linhas_2, n_colunas_2):

    # as matrizes devem existir dentro da função
    matriz_1 = []
    matriz_2 = []

    # validação
    if n_colunas_1 != n_linhas_2:
        print("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda!")
        return

    # entrada matriz 1
    for i in range(n_linhas_1):
        linha = []
        for j in range(n_colunas_1):
            b = int(input(f"Digite o item {j+1} da linha {i+1} da Matriz 1: "))
            linha.append(b)
        matriz_1.append(linha)

    # entrada matriz 2
    for i in range(n_linhas_2):
        linha = []
        for j in range(n_colunas_2):
            b = int(input(f"Digite o item {j+1} da linha {i+1} da Matriz 2: "))
            linha.append(b)
        matriz_2.append(linha)

    # matriz resultado (linhas da primeira x colunas da segunda)
    resultado = [[0 for _ in range(n_colunas_2)] for _ in range(n_linhas_1)]

    # multiplicação
    for i in range(n_linhas_1):
        for j in range(n_colunas_2):
            for k in range(n_colunas_1):  # ou n_linhas_2, tanto faz
                resultado[i][j] += matriz_1[i][k] * matriz_2[k][j]

    # saída
    print("\nResultado:")
    for row in resultado:
        print(row)



print("Adição [0]\nSubtração [1]\nMultiplicação [2]\n")
calculo = int(input("Selecione o tipo de operação: "))
if calculo==0:

    n_linhas=int(input("\nNúmero de linhas das matrizes: "))
    n_colunas=int(input("\nNúmero de colunas das matrizees: "))

    Adição(n_linhas,n_colunas)

elif calculo==1:

    n_linhas=int(input("\nNúmero de linhas das matrizes: "))
    n_colunas=int(input("\nNúmero de colunas das  matrizes: "))

    Subtracao(n_linhas,n_colunas)

elif calculo ==2:

    n_linhas_1=int(input("\nNúmero de linhas da primeira matriz: "))
    n_colunas_1=int(input("\nNúmero de colunas da primeira matriz: "))

    n_linhas_2=int(input("\nNúmero de linhas da segunda matriz: "))
    n_colunas_2=int(input("\nNúmero de colunas da segunda matriz: "))

    Multiplicacao(n_linhas_1,n_colunas_1,n_linhas_2,n_colunas_2)

else:
    print("\nSelecione uma das opções disponiveis (só a soma no momento)\n")

