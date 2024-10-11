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