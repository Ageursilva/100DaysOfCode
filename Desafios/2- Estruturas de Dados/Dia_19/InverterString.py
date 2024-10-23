def inverter_string():
    texto=str(input("Por favor, digite um texto para ser invertido: "))
    texto_invertido=''.join(reversed(texto))
    print("O texto invertido e: ", texto_invertido)

inverter_string()