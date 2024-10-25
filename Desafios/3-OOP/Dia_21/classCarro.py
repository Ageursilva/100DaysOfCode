class carro:
    def __init__(self,marca,ano,modelo,kilometragem,combustivel,tranmissao,preço):
        self.marca = marca
        self.ano = ano
        self.modelo= modelo
        self.kilometragem = kilometragem
        self.combustivel=  combustivel
        self.tranmissao= tranmissao
        self.preço= preço
    pass

carro_viagem = carro('Fiat', 2018, 'Palio', 0, 'Gasolina', 'Manual', 10000)

print(carro_viagem.__dict__)

print(carro_viagem.marca,carro_viagem.ano,carro_viagem.modelo,carro_viagem.kilometragem,carro_viagem.combustivel,carro_viagem.tranmissao,carro_viagem.preço)