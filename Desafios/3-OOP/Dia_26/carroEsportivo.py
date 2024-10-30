import car

class carro(car.car):
    def __init__(self, marca,ano,modelo,kilometragem,combustivel,transmissao,preco,cor, numero_portas,cilindros, cilindradas):
        super().__init__(marca, ano, modelo, kilometragem, combustivel, transmissao, preco,cor,numero_portas)
        self.cilindros = cilindros
        self.cilindradas = cilindradas

    def ligar(self):
        print("Ligando o carro...")

    def desligar(self):
        print("Desligando o carro...")

    def acelerar(self):
        print("Acelerando o veículo...")

    def frear(self):
        print("Ferando o veículo...")

    def virar_direcao(self):
        print("virando a direção...")
        
    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
        print(f"Modelo: {self.modelo}")
        print(f"Kilometragem: {self.kilometragem}")
        print(f"Combustível: {self.combustivel}")
        print(f"Transmissão: {self.transmissao}")
        print(f"Preço: {self.preco}")
        print(f"Cilindos: {self.cilindros}")
        print(f"Cilindradas: {self.cilindradas}")
    
carro_viagem = carro('Fiat', 2018, 'Palio', 0, 'Gasolina', 'Manual', 10000,'verde','4',250,300)

carro_viagem.ligar()
carro_viagem.exibir_dados()
carro_viagem.desligar()