def encontrar_maior_e_menor(lista):
    if not lista:
        return None, None  

    maior = lista[0] 

    for numero in lista:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    return maior, menor

numeros = [15, 3, 9, 21, -5, 7, 3]
maior, menor = encontrar_maior_e_menor(numeros)
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")