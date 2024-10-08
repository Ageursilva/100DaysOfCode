print("Este programa conta quantas vezes cada vogal aparece em uma frase.")
frase=input("Por favor, digite uma frase: ").strip().lower()
def contar_vogais(frase):

    vogais = "aeiou"
    vogais="aeiou"
    for i in vogais:
        print(f"A letra '{i.upper()}' aparece {frase.count(i)} vezes na frase")
    return

contar_vogais(frase)

