'''print("Olá mundo!")
print('Tô aqui.')

nome = 'Sandro'
idade = 22
peso = 88.9
sexo = "m"
masc = True

print("O nome é: " + nome + "idade " + str(idade) + " peso " + str(peso) + " sexo " + sexo)

valor = idade + peso

print(valor)

idade1 = '22'
idade2 = '33'

print(idade1 + idade2)

print(type(idade1))
print(type(idade))
print(type(peso))
print(type(sexo))
print(type(masc))

print(3+3)
print(3*3)
print(3**3)
print(3/3)
print(3%3)

print('='*50)

x = 10
y = 10

print(x>y)
print(x<y)
print(x==y)
print(x>=y)
print(x<=y)
print(x!=y)
'''

'''
nome = input("Digite seu nome: ")
idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso: "))

print("O nome do cliente é ", nome, " ele tem ", idade, " anos e pesa ", peso, " Kg")
'''

ano_nascimento = int(input("Informe seu ano de nascimento: "))
ano_atual = int(input("Informe o ano atual: "))

idade = ano_atual - ano_nascimento

if idade<0:
    print("Informe um ano válido!")
else:
    print("A sua idade é ", idade, " anos.")




