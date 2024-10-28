class livro:
    def __init__(self, nome, autor, ano, editora,categoria):
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.categoria = categoria
        
    def __str__(self):
        return f'Titulo: {self.nome}\nAutor: {self.autor}\nAno: {self.ano}\nEditora: {self.editora}\nCategoria: {self.categoria}'
    
class Biblioteca:
    def __init__(self):
        self.livros = []
    def adicionar_livros(self):
        nome = input("Digite o nome do livro: ").strip().capitalize()
        autor = input("Digite o nome do autor do livro: ").strip().capitalize()
        ano = input("Data de publicação do livro: ").strip()
        editora = input("Digite o nome da editora do livro: ").strip().capitalize()
        categoria = input("Digita qual a categoria do livro: ").strip().capitalize()
        novo_livro = livro(nome, autor, ano, editora, categoria)
        self.livros.append(novo_livro)
        print(f"O Livro {nome} foi adicionado com sucesso!")
    def remover_livros(self):
        nome = input("Qual o nome do livro que deseja remover?: ").strip().capitalize()
        for livro in self.livros:
            if livro.nome == nome:
                self.livros.remove(livro)
                print(f"O livro {nome} foi removido!")
                return
        print(f"O livro {nome} nao foi encontrado na biblioteca, por favor tente novamente!")
        
    def buscar_livros(self):
        nome=input("Qual o nome do livro que deseja buscar?: ").strip().capitalize()
        for livro in self.livros:
            if livro.nome == nome:
                print(livro)
                return
            print(f"O livro {nome} foi encontrado na biblioteca!")
    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro encontrado na biblioteca")
        else:
            for livro in self.livros:
                for i ,livro in enumerate(self.livros,1):
                    print("Livros disponíveis na biblioteca:")
                    print(50*"-")
                    print(f'\nLivro {i}:')
                    print(livro)
                    print(50*"-")
def menu():
    print("Selecione uma das seguintes opções:")
    print("1 - Cadastrar um novo livro")
    print("2 - Remover livro")
    print("3 - Buscar livros disponíveis")
    print("4 - Listar livros disponíveis")
    print("5 - Sair")
    escolha= str(input('Qual opçao deseja escolher? '))	
    return escolha
    
    
def main():
    biblioteca = Biblioteca()
    while True:
        opcao = menu()
        if opcao == '1':
            biblioteca.adicionar_livros()
        elif opcao == '2':
            biblioteca.remover_livros()
        elif opcao == '3':
            biblioteca.buscar_livros()
        elif opcao == '4':
            biblioteca.listar_livros()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()