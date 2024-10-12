lista = []

def lista_de_compras():
    print("Bem-vindo à lista de compras!")
    print(50 * "-")
    print("1 - Adicionar produto na lista de compras")
    print("2 - Remover produto da lista de compras")
    print("3 - Mostrar lista de compras")
    print("4 - Sair")
    escolha = str(input('Escolha uma opção: '))

    if escolha == '1':
        produto = input("Por favor, digite o nome do item que deseja adicionar à lista: ").strip().capitalize()
        lista.append(produto)  # Operação push
        print(f"O produto {produto} foi adicionado à lista de compras!")
        lista_de_compras()
    elif escolha == '2':
        if len(lista) == 0:
            print("A lista está vazia!")
        else:
            produtoRemovido = lista.pop()  # Operação pop
            print(f"O produto {produtoRemovido} foi removido da lista de compras!")
        lista_de_compras()
    elif escolha == '3':
        if len(lista) == 0:
            print("A lista está vazia!")
        else:
            print("Lista de compras:", ", ".join(lista))
        lista_de_compras()
    elif escolha == '4':
        print("Obrigado por utilizar a lista de compras!")
    else:
        print("Opção inválida. Por favor, tente novamente!")
        lista_de_compras()

lista_de_compras()
