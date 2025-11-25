def censurar(cpf):
    try:
        cpf_numeros = cpf.replace(".", " ").replace("-"," ") #transforma os "." e "-" em espaços

        cpf_em_lista = cpf_numeros.split()# separa os numeros em uma lista 

        for index, cpf_str in enumerate(cpf_em_lista): # esse enumerate atribui um valor a cada membro da lista

            if len(cpf_em_lista[index]) < 4 and len(cpf_em_lista[index]) > 2: # o len lê os caracteres 

                cpf_em_lista[index] ="###"

                cpf_censurado=" ".join(cpf_em_lista)

        return print("Seu CPF censurado é: ",cpf_censurado)
    except:
        return print("Digite o CPF como demonstrado: 000.000.000-00")

cpf = input("Digite seu CPF (000.000.000-00): ")

censurar(cpf)

#import re ESSE É FEITO POR IA( ESTUDE )

#def censurar(cpf: str) -> str:
    #cpf = cpf.strip()
    #m = re.fullmatch(r'(\d{3})\.(\d{3})\.(\d{3})-(\d{2})', cpf)
    #if not m:
     #   raise ValueError("Formato inválido: use 000.000.000-00")
    #a, b, c, d = m.groups()
    #return f"###.{ '###' if len(b)==3 else b }.{ '###' if len(c)==3 else c }-{d}"

#if __name__ == "__main__":
 #   cpf = input("Digite seu CPF (000.000.000-00): ")
  #  try:
   #     print("Seu CPF censurado é:", censurar(cpf))
    #except ValueError as e:
     #   print(e)