while True:
    nome=input("Por favor, digite seu nome: ").strip().title()
    
    if not nome.isalpha():
        print("Nome não pode estar vazio e somente pode conter letras.Por favor, tente novamente!")
    else:
        print(f'Olá, {nome}! Seja bem-vindo(a)!')
        break