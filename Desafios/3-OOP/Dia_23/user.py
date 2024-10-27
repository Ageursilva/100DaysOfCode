import hashlib
class user:
    
    def __init__(self, nome_usuariio, senha):
        self.nome_usuariio = nome_usuariio
        self.senha_hash = self.gerar_hash(senha)
        
    def gerar_hash(self,senha):
        return hashlib.sha256(senha.encode()).hexdigest()    
        
    def registro(self,nome_usuario,senha,banco_dados):
        if nome_usuario in banco_dados:
            return "Erro: Usuário ja cadastrado"
        
        novo_user = user(nome_usuario,senha)
        banco_dados[novo_user.nome_usuariio] = novo_user
        return "Usário criado com sucesso"
    
    def login(self,nome_usuario,senha,banco_dados):
        if nome_usuario not in banco_dados:
            return "Erro: Usuário nao cadastrado"
        
        user = banco_dados[nome_usuario]
        
        if user.senha_hash == user.gerar_hash(senha):
            return "Login efetuado com sucesso"
        else:
            return "Erro: Senha incorreta"
        
        
        
banco_dads ={}

usuario = user("teste","123")

print (usuario.registro("teste","123",banco_dads))
print(usuario.login("teste","153",banco_dads)) 
       