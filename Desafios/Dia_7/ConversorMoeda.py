def conversor():
    print("Selecione o valor que deseja converter para Real:")
    print("1 - Dólar")
    print("2 - Euro")
    print("3 - Libra")
    print("4 - Yuan")
    escolha= str(input('Escolha uma opção: '))
    
    if escolha == '1':
        valor = float(input("Por favor, digite o valor que deseja converter: "))
        print(f"{valor} Dólar(s) equivalem a R$ {valor * 5.44}")
    elif escolha == '2':
        valor = float(input("Por favor, digite o valor que deseja converter: "))
        print(f"{valor} Euro(s) equivalem a R$ {valor * 5.99}")
    elif escolha == '3':
        valor = float(input("Por favor, digite o valor que deseja converter: "))
        print(f"{valor} Libra(s) equivalem a R$ {valor * 7.14}")
    elif escolha == '4':
        valor = float(input("Por favor, digite o valor que deseja converter: "))
        print(f"{valor} Yuan(s) equivalem a R$ {valor * 0.78}")
    else:
        print("Opção inválida. Por favor, tente novamente!")
    return

conversor()

