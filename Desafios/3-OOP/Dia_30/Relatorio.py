from datetime import datetime
from typing import List, Dict

class Relatorio:
    def __init__(self,titulo:str):
        self.titulo = titulo
        self.data_geracao = datetime.now()
        self.secoes: List[Secao] = []
        
    def adicionar_secao(self,titulo: str) ->'Secao':
        secao = Secao(titulo)
        self.secoes.append(secao)
        return secao
    def gerar(self)-> str:
        conteudo =[]
        
        #cabecalho
        conteudo.append("=" * 50)
        conteudo.append(f"{self.titulo.center(50)}")
        conteudo.append(f"Gerado em: {self.data_geracao.strftime('%d/%m/%Y %H:%M')}")
        conteudo.append("=" * 50)
        conteudo.append("")
        
        #seções
        
        for secao in self.secoes:
            conteudo.append(secao.gerar())
            conteudo.append("")
            
        return "\n".join(conteudo)
    def salvar (self,nome_arquivo:str):
        with open(nome_arquivo,"w", encoding='utf-8') as f:
            f.write(self.gerar())

class Secao:
    def __init__(self,titulo:str):
        self.titulo = titulo
        self.itens: List[Dict] = []
    def adicionar_item(self,descricao:str,valor:any):
        self.itens.append({"descricao":descricao,"valor":valor})
        
    def gerar(self)->str:
        conteudo = []
         # Título da seção
        conteudo.append(f"{self.titulo}")
        conteudo.append("-" * len(self.titulo))
        
        # Itens
        for item in self.itens:
            conteudo.append(f"{item['descricao']}: {item['valor']}")
            
        return "\n".join(conteudo)

# Exemplo de uso
if __name__ == "__main__":
    
    # Criando um relatório de vendas
    relatorio = Relatorio("Relatório de Vendas Mensal")
    
    # Adicionando seção de métricas gerais
    metricas = relatorio.adicionar_secao("Métricas Gerais")
    metricas.adicionar_item("Total de Vendas", "R$ 150.000,00")
    metricas.adicionar_item("Quantidade de Pedidos", 1500)
    metricas.adicionar_item("Ticket Médio", "R$ 100,00")
    
    # Adicionando seção de produtos mais vendidos
    produtos = relatorio.adicionar_secao("Produtos Mais Vendidos")
    produtos.adicionar_item("1º Lugar", "Smartphone X - 500 unidades")
    produtos.adicionar_item("2º Lugar", "Notebook Y - 300 unidades")
    produtos.adicionar_item("3º Lugar", "Tablet Z - 200 unidades")
    
   
    print(relatorio.gerar())  
    relatorio.salvar("relatorio_vendas.txt")                