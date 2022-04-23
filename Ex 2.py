nome = input("Qual seu nome: ")
dia = int(input("Qual dia você nasceu: "))
mês = input("Qual mês que você nasceu(extenso): ")
ano = int(input ("Qual ano que você nasceu (aaaa): "))
ano_atual = 2022-ano
print("Olá {}".format(nome))
print("No dia {} de {} parabens pelo seu aniversário de {} anos". format(dia,mês,ano_atual))
