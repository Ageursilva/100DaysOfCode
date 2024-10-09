def calculadoraImc():
    print("Digie seu dados para saber seu IMC")
    peso = float(input("Por favor, digite o seu peso: "))
    altura = float(input("Por favor, digite a sua altura: "))
    imc = peso / (altura ** 2)
    print(f"Seu IMC é:  {imc:.2f}")
    if imc < 18.5:
        print("Com base no seu ICM você esta abaixo do peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Com base no seu ICM você esta com o peso normal")
    elif imc >= 25 and imc <= 29.9:
        print("Com base no seu ICM você esta acima do peso")
    elif imc >= 30 and imc <= 34.9:
        print("Com base no seu ICM você esta em obesidade I")
    elif imc >= 35 and imc <= 39.9:
        print(" Com base no seu ICM você esta obesidade II")
    elif imc >= 40:
        print("Com base no seu ICM você esta obesidade III")
    return imc

calculadoraImc()