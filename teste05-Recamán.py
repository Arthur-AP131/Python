a = int(input("Digite um número: "))
b=[]
resul_anterior=0
for i in range(a):
    if i == 0:
        b.append(i)
    else:
        if (b[i-1] - i) > 0 and (b[i-1] - i) not in b:
            b.append(b[i-1] - i)
        else:
            b.append(b[i-1] + i) 
print(b)