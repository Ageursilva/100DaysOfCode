class carro:
    def __init__(self,marca,ano,modelo,kilometragem,combustivel,transmissao,preço):
        self.marca = marca
        self.ano = ano
        self.modelo= modelo
        self.kilometragem = kilometragem
        self.combustivel=  combustivel
        self.transmissao= transmissao
        self.preço= preço
        
    def ligar(self):
        print("Ligando o carro...")
        
    def desligar(self):
        print("Desligando o carro...")
    
    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
        print(f"Modelo: {self.modelo}")
        print(f"Kilometragem: {self.kilometragem}")
        print(f"Combustível: {self.combustivel}")
        print(f"Transmissão: {self.tranmissao}")
        print(f"Preço: {self.preço}")
carro_viagem = carro('Fiat', 2018, 'Palio', 0, 'Gasolina', 'Manual', 10000)

carro_viagem.ligar()
carro_viagem.exibir_dados()
carro_viagem.desligar()