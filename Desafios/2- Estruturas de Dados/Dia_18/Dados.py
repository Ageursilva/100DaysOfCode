from random import randint

def rolar_dados():
    print('Este programa serve para rolar dadods de 6 lados')
    dados=int(input('Quantos dados deseja rolar? '))
    for i in range(dados):
        print("Rolando dados de 6 lados: ",randint(1, 6))
        
        
rolar_dados()

