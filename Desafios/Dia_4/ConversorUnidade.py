def menu():
    print("Selecione uma das seguintes opções:")
    print("1 - Calculadora")
    print("2 - Conversor de unidades")
    escolha= str(input('Escolha uma opção: '))
    return escolha
opcao = menu() 

def calculadora():
    operacao = input("Por favor, digite a operação que deseja realizar: +, -, / ou *: ").strip().lower()
    numero_1 = float(input("Por favor, digite o primeiro número: ").strip())
    numero_2 = float(input("Por favor, digite o segundo número: ").strip())
    if operacao == "+":
        print(f"O resultado da operação {numero_1} + {numero_2} é {numero_1 + numero_2}")
    elif operacao == "-":
        print(f"O resultado da operação {numero_1} - {numero_2} é {numero_1 - numero_2}")
    elif operacao == "/":
        print(f"O resultado da operação {numero_1} / {numero_2} é {numero_1 / numero_2}")
    elif operacao == "*":
        print(f"O resultado da operação {numero_1} * {numero_2} é {numero_1 * numero_2}")
    else:
        print("Operação inválida. Por favor, tente novamente!")
    return
def conversor():
    fahrenheit= int(input("Por favor, digite a temperatura em Fahrenheit: "))
    celsisus= (5/9) * (fahrenheit - 32)
    print(f"{fahrenheit}°F = {celsisus}°C")
    return

if opcao == '1': 
    calculadora()
if opcao == '2':    
    conversor()
  