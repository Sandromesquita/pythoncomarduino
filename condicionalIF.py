print("AULA 02 - CONDICIONAL IF")

"""Recebe 3 notas, calcula a média e se for maior que 7 retorna aprovado
se for menor que 7 retorna reprovado"""

n1 = float(input("Insira a nota 01: "))
n2 = float(input("Insira a nota 02: "))
n3 = float(input("Insira a nota 03: "))

m = (n1 + n2 + n3) / 3

'''print("A média do aluno é: ", m)'''

if m >= 7:
    print("O aluno passou com média: ", m)

elif 7 > m >= 4:
    print("O aluno de recuperação com média: ", m)
    nr = float(input("Insira a nota de recuperação: "))
    r = (nr + m) / 2
    if r >= 7:
        print("O aluno passou com média de recuperação: ", r)

    else:
        print("O aluno reprovou com média de recuperação: ", r)

else:
    print("O aluno reprovou com média: ", m)
