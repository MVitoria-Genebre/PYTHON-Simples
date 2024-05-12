soma = 0

while True:
    num = float(input("Insira um valor: "))
    num2 = float(input("Insira um valor: "))

    if num == 0 or num2 == 0:
        break

    resultado = num + num2
    soma += 1

    print(f"A soma de {num} + {num2} corresponde a:{resultado}")
    print(f" Total de somas realizadas: {soma}")