def contador_palavras(texto):
    texto = texto.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    palavras = texto.split()
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia

texto = "Olá mundo! Este é um texto simples. Este texto é apenas um exemplo de texto."
frequencia_palavras = contador_palavras(texto)
print(frequencia_palavras)