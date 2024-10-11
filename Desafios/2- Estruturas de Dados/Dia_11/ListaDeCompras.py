
lista = []
def lista_de_compras():
    print("Bem vindo a lista de coompras!")
    print(50*"-")
    print("1 - Adicionar produto na lista de compras")
    print("2 - Remover produto na lista de compras")
    print("3 - Mostrar lista de compras")
    print("4 - Sair")
    escolha= str(input('Escolha uma opção: '))

    if escolha == '1':
        produto = input("Por favor, digite o nome do item que deseja adicionar a lista: ").strip().capitalize()
        lista.append(produto)
        print(f" O produto {produto} foi adicionado a lista de compras!")
        lista_de_compras()
    elif escolha == '2':
        produtoRemovido = input("Por favor, digite o nome do item que deseja excluir da lista: ").strip().capitalize()
        lista.remove(produtoRemovido)
        print(f" O produto {produtoRemovido} foi removido da lista de compras!")
        lista_de_compras()       
    elif escolha == '3':
        print(f"Lista de compras: {lista}")
        lista_de_compras()
    elif escolha == '4':
        print("Obrigado por utilizar a lista de compras!")
        quit()
    else:
        print("Opção inválida. Por favor, tente novamente!")
        lista_de_compras()
    return lista

lista_de_compras()


