import itertools

def gera_anagramas(palavra):
    palavra = palavra.replace(" ", "").lower()
    permutacoes = itertools.permutations(palavra)
    anagramas = set("".join(p) for p in permutacoes)
    
    return anagramas

palavra = input("Digite uma palavra: ")
anagramas = gera_anagramas(palavra)

print("Os anagramas posiveis são::")
for anagrama in anagramas:
    print(f"- {anagrama}")