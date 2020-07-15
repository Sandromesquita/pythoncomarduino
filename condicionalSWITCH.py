print("AULA 02 - CONDICIONAL SWITCH/CASE gambiarra")

x = int(input("Digite um numero: "))

if x is 0:
    print("Você esta na porta zero.")

elif x in (1, 3):
    print("Você esta na porta um ou na tres.")

elif x is 2:
    print("Você esta na porta dois.")

else:
    print("Você esta na porta avulsa.")

