print("Bem vindo a calculadora de tabuada, sinta-se a vontade para fazer qualquer tabuada")


while True:
    numero = int(input("Digite o número da tabuada: "))

    if numero < 0:
        print("Não é permitido números negativos")
        continue

    limite = int(input("Digite até qual número a tabuada deve ir: "))

    if limite < 0:
        print("Não é permitido número negativo")
        continue
    
    contador = 0

    while contador <= limite:
        print(f"{numero}x{contador}={numero * contador}")
        contador += 1

    opcao = input("Deseja gerar outra tabuada? (S/N): ") .upper()

    if opcao != "S":
        print("Programa encerrado.")
        break
