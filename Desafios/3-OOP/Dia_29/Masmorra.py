import random
from typing import List

class Sala:
    def __init__(self, nome: str, descricao: str, tem_monstro: bool = False, tem_tesouro: bool = False):
        self.nome = nome
        self.descricao = descricao
        self.tem_monstro = tem_monstro
        self.tem_tesouro = tem_tesouro
        self.visitado = False

class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.vida = 100
        self.tesouro = 0
        self.esta_vivo = True
    
    def sofrer_dano(self, dano: int):
        self.vida -= dano
        if self.vida <= 0:
            self.esta_vivo = False
            self.vida = 0
    
    def coletar_tesouro(self):
        self.tesouro += 1

class Jogo:
    def __init__(self):
        self.salas = self.criar_salas()
        self.sala_atual = 0
        print("Bem-vindo ao jogo de Masmorra!")
        nome = input("Digite o nome do seu aventureiro: ")
        self.jogador = Jogador(nome)
    
    def criar_salas(self) -> List[Sala]:
        return [
            Sala("Entrada", "Uma sala escura com paredes de pedra. Há teias de aranha por todo lado."),
            Sala("Corredor", "Um longo corredor úmido. Você ouve gotas de água caindo.", True),
            Sala("Biblioteca", "Uma antiga biblioteca empoeirada. Livros cobrem as paredes.", False, True),
            Sala("Sala do Tesouro", "Uma sala brilhante com ouro espalhado!", False, True),
            Sala("Câmara Final", "Uma grande câmara circular com um altar no centro.", True)
        ]
    
    def mostrar_status(self):
        print(f"\nVida: {self.jogador.vida} | Tesouros: {self.jogador.tesouro}")
        print(f"Localização atual: {self.salas[self.sala_atual].nome}")
        print(self.salas[self.sala_atual].descricao)
    
    def combate(self):
        print("\nUm inimigo apareceu!")
        dano = random.randint(10, 30)
        self.jogador.sofrer_dano(dano)
        print(f"O inimigo causou {dano} de dano em você!")
    
    def verificar_tesouro(self):
        sala = self.salas[self.sala_atual]
        if sala.tem_tesouro and not sala.visitado:
            self.jogador.coletar_tesouro()
            print("\nParabéns, você encontrou um tesouro!")
            sala.visitado = True
    
    def jogar(self):
        while self.jogador.esta_vivo and self.sala_atual < len(self.salas):
            self.mostrar_status()
            sala_atual = self.salas[self.sala_atual]
            
            if sala_atual.tem_monstro and not sala_atual.visitado:
                self.combate()
                sala_atual.visitado = True
            
            if not self.jogador.esta_vivo:
                print("\nVocê foi morto! Game Over!")
                break
            
            self.verificar_tesouro()
            
            if self.sala_atual == len(self.salas) - 1:
                print("\nParabéns! Você chegou ao final do jogo!")
                break
            
            input("\nPressione Enter para avançar...")
            self.sala_atual += 1
        
        print(f"\nFim de jogo! Você coletou {self.jogador.tesouro} tesouros!")

if __name__ == "__main__":
    jogo = Jogo()
    jogo.jogar()
