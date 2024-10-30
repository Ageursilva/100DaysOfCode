class car():
    def __init__(self,marca,ano,modelo,kilometragem,combustivel,transmissao,preco,cor, numero_portas):
        self.marca = marca
        self.ano = ano
        self.modelo= modelo
        self.cor= cor
        self.numero_portas= numero_portas
        self.kilometragem = kilometragem
        self.combustivel=  combustivel
        self.transmissao= transmissao
        self.preco= preco
        
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
        