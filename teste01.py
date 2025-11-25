def adicionarCu (x):
    return x + "cu"

a = list(input("Digite algo: ").split())# separa a frase nos espaços e faz cada palavra em um item da lista

b = list(map(adicionarCu, a)) #map pega uma função e uma lista e passa essa lista como um parametro

c = " ".join(b) #transforma a lista em string 

print(c)

    