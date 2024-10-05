def gerador_de_senha():
    import random
    import string
    quantidadeCaracteres = int(input("Por favor, digite a quantidade de caractes que você quer a senha: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation+string.ascii_uppercase
    password = "".join(random.choice(caracteres) for i in range(quantidadeCaracteres))
    print (f"Sua senha é: {password}"  )
    nova_senha = input("Deseja gerar uma nova senha? (s/n): ")
    if nova_senha == "s":
        gerador_de_senha()
    elif nova_senha == "n":
        print("Obrigado por utilizar o gerador de senha")
    else:
        print("Opcão inválida")
        gerador_de_senha()
gerador_de_senha()

