import random
def jogo_adivinha():
    print("Bem-vindo ao jogo de adivinhacão!")
    print("Eu irei pensar em um número entre 0 e 100. Tente adivinhar qual é.")
    numero_sorteado=random.randint(0,100)
    tentativa = 0
    tentativa_maximas = 3
    
    while tentativa < tentativa_maximas:
          palpite = int(input("Adivinhe o número entre 0 e 100: "))
          tentativa += 1         
          if palpite == numero_sorteado:
              print(f"Parabéns, voce acertou!.O número era {numero_sorteado}")
          else:
              print("Infelizmente, voce errou. Tente novamente.")
    
    if tentativa == tentativa_maximas:
        print(f"Infelizmente, voce perdeu. O número era {numero_sorteado}.")  


jogo_adivinha()