class Banco:
    def __init__(self, nome, cpf, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
            
    def mostrar_saldo(self):
        print(f'Seu saldo atual é R${self.saldo:.2f}')
        
    
def menu():
    print("Selecione uma das seguintes opções:")
    print("1 - Mostrar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    escolha = input('Qual opção deseja escolher? ')	
    return escolha
    
    
def main():
    print("Bem vindo ao seu banco!")
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    banco = Banco(nome, cpf)

    while True:
        opcao = menu()
        if opcao == '1':
            banco.mostrar_saldo()
        elif opcao == '2':
            valor = float(input("Qual o valor que deseja depositar?: "))
            banco.depositar(valor)
        elif opcao == '3':
            valor = float(input("Qual o valor que deseja sacar?: "))
            banco.sacar(valor)
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()
