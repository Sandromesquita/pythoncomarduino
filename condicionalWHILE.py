print("AULA 02 - CONDICIONAL WHILE")

"""O usuário insere numeros até der na telha"""

soma = 0
contador = 0
resp = 's'

while resp == 's':
    contador = contador +1
    n = int(input("Escreva um numero: "))
    print("O numero digitado foi: ", n)
    soma = soma + n
    print("="*50)
    resp = input("Deseja escrever outro numero? [s/n]: ")

m = soma/contador
print("Programa encerrado, a média dos numeros é: ", m)
