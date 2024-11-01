class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
        self.ligado = False
    
    def ligar(self):
        if not self.ligado:
            print(f"{self.marca} {self.modelo} está ligando...")
            self.ligado = True
        else:
            print("O carro já está ligado!")
    
    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print(f"Acelerando... Velocidade atual: {self.velocidade} km/h")
        else:
            print("Não é possível acelerar com o carro desligado!")

class CarroEsportivo(Carro):
    def __init__(self, marca, modelo, turbo=False):
        super().__init__(marca, modelo)
        self.turbo = turbo
    
    def acelerar(self):  # Sobrescrevendo o método acelerar
        if self.ligado:
            if self.turbo:
                self.velocidade += 30
                print(f"VRUUM! Acelerando com turbo... Velocidade atual: {self.velocidade} km/h")
            else:
                self.velocidade += 20
                print(f"Acelerando modo esportivo... Velocidade atual: {self.velocidade} km/h")
        else:
            print("Não é possível acelerar com o carro desligado!")

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, nivel_bateria=100):
        super().__init__(marca, modelo)
        self.nivel_bateria = nivel_bateria
    
    def ligar(self):  # Sobrescrevendo o método ligar
        if not self.ligado and self.nivel_bateria > 0:
            print(f"{self.marca} {self.modelo} iniciando sistemas elétricos...")
            self.ligado = True
        elif self.nivel_bateria <= 0:
            print("Bateria descarregada! Precisa recarregar.")
        else:
            print("O carro já está ligado!")
    
    def acelerar(self):  # Sobrescrevendo o método acelerar
        if self.ligado and self.nivel_bateria > 0:
            self.velocidade += 15
            self.nivel_bateria -= 2
            print(f"Acelerando silenciosamente... Velocidade: {self.velocidade} km/h, Bateria: {self.nivel_bateria}%")
        elif self.nivel_bateria <= 0:
            print("Bateria descarregada! Precisa recarregar.")
        else:
            print("Não é possível acelerar com o carro desligado!")

# Exemplo de uso
def testar_carro(carro):
    print(f"\nTestando {type(carro).__name__}: {carro.marca} {carro.modelo}")
    carro.ligar()
    carro.acelerar()
    carro.acelerar()
    
# Criando diferentes tipos de carros
carro_normal = Carro("Volkswagen", "Gol")
carro_esportivo = CarroEsportivo("Ferrari", "F8", turbo=True)
carro_eletrico = CarroEletrico("Tesla", "Model 3")

# Testando cada carro
testar_carro(carro_normal)
testar_carro(carro_esportivo)
testar_carro(carro_eletrico)