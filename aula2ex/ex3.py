def main():
    nomes = input("Digite a lista de nomes ")
    nomes_lista = nomes.split(',')
    nomes__lista_limpos = []

    for nome in nomes_lista:
        nome = nome.strip()
        nomes__lista_limpos.append(nome)

    print("A lista de nomes é:", nomes__lista_limpos)

if __name__ == "__main__":
    main()
