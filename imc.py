
iniciar = True

while iniciar:
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))

    imc = peso / (altura ** 2) #Formula do IMC
    print(f"Seu IMC é: {imc}")

    resposta = input("Deseja calcular outro IMC? (s/n): ")
    if resposta.lower() != 's':
        iniciar = False