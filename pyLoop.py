m=0

def calculadora(x=3, y=0, z=0):
    global m
    m = x + y + z
    print("A soma temporária é: {}.".format(m))

#PROGRAMA PRINCIPAL
while True:
    print("programa principal!")
    x = int(input("Digite outro numero: "))
    y = int(input("Digite outro numero: "))
    z = int(input("Digite outro numero: "))
    calculadora(x)
    calculadora(x, z)
    calculadora(x, y, z)
    calculadora(y, z)
    if m > 30:
        print("Sua conta estourou.")
        break

print("Não entrei em canto nenhum.")




