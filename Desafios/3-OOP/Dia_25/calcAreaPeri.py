class retangulo:
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura
    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
print("Esse programa calcula a area e o perimetro de um retangulo")
largura = float(input("Digite a largura do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))

print(f"Area = {retangulo(largura,altura).area()}")
print(f"Perimetro = {retangulo(largura,altura).perimetro()}" )    