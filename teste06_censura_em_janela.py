import tkinter as tk 


resultado = ""

def censurar(cpf):
    try:
        cpf_numeros = cpf.replace(".", " ").replace("-"," ") #transforma os "." e "-" em espaços

        cpf_em_lista = cpf_numeros.split()# separa os numeros em uma lista 

        for index, cpf_str in enumerate(cpf_em_lista): # esse enumerate atribui um valor a cada membro da lista

            if len(cpf_em_lista[index]) < 4 and len(cpf_em_lista[index]) > 2: # o len lê os caracteres 

                cpf_em_lista[index] ="***"

                cpf_censurado=" ".join(cpf_em_lista)

        return "Seu CPF censurado é: ",cpf_censurado
    except:
        return "Digite o CPF como demonstrado: 000.000.000-00" 
    
def chamar_censura():
    texto = input_CPF.get()
    resultado = censurar(texto)
    label_resultado.config(text=resultado)


janela = tk.Tk()
janela.title = "Censura CPF em janela"
janela.geometry('500x400')

Label_censura = tk.Label(janela, text="Inseria abaixo o seu CPF")
Label_censura.pack(pady=50)

input_CPF= tk.Entry()
input_CPF.pack()

botão = tk.Button(text="censurar", command= chamar_censura)
botão.pack(pady=20)

label_resultado = tk.Label(janela, text=f" ")
label_resultado.pack(pady=20)



janela.mainloop()
