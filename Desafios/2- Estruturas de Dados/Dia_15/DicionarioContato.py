meus_contatos = {
    'josé': "11000000000",
    'Maria': "12000000000",
    'Joaquim': "13000000000",
    'Marioo': "14000000000",
    'João': "15000000000"
}

def adicionar_contato():
    nome = input("Digite o nome do contato: ").strip().capitalize()
    numero = input("Digite o número do contato: ").strip()
    
    if nome in meus_contatos:
        print(f"O contato {nome} já existe com o número {meus_contatos[nome]}.")
    else:
        meus_contatos[nome] = numero
        print(f"Contato {nome} adicionado com sucesso!")

# Exemplo de uso
adicionar_contato()
print("Lista de contatos atualizada:")
print(meus_contatos)