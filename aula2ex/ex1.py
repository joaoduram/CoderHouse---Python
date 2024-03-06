def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def main():
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em metros: "))
    imc = calcular_imc(peso, altura)
    print("O IMC é:", imc)

if __name__ == "__main__":
    main()
