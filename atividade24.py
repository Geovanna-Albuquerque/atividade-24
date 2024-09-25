
def calcular_media():
    soma = 0
    contador = 0

    while True:
        try:
            numero = float(input("Digite um número (-1 para encerrar): "))
            
            if numero == -1:
                break

            soma += numero
            contador += 1except ValueError:
            print("Por favor, digite um número válido.")

    if contador > 0:
        media = soma / contador
        print(f"A média dos números digitados é: {media:.2f}")
    else:
        print("Nenhum número válido foi digitado.")

if __name__ == "__main__":
    calcular_media()