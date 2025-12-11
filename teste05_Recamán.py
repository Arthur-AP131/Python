a = int(input("Digite um número: ")) 
b=[]# a lista que vai conter toda a sequecia

for i in range(a):
    if i == 0: # faz com que a sequecia sempre comece com o zero 
        b.append(i)
    else: # unica linha do codigo gerado por IA pq sou burro. toda vez que o numero não for 0 ativa essa else
        if (b[i-1] - i) > 0 and (b[i-1] - i) not in b:# se o resultado da conta (b[i-1] - i) for maior que 0 e não estiver na sequencia ele adiciona o resultado na sequecia
            b.append(b[i-1] - i)
        else: # se for menor que zero ou estiver na sequencia ele adiciona  b[i-1] + i 
            b.append(b[i-1] + i) 
print(b) # mostra a sequecia