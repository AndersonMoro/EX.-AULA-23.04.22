print("\033[1;31mNOTAS E MEDIAS\033[0;0m")
aluno = input("Qual nome do aluno: ")
n1 = float(input("Qual primeira nota: "))
n2 = float(input("Qual a segunda nota: "))
n3 = float(input("Qual a terceira nota: "))
media = (n1+n2+n3) / 3
print("O aluno {} teve as seguintes notas: {},  {},  {}. \n A média foi {}".format(aluno,n1,n2,n3,media))