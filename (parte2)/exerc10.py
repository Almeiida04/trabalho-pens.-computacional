def filtrar(texto, denylist):
    texto_lower = texto.lower()
    denylist_lower = [palavra.lower() for palavra in denylist]
    palavras = texto_lower.split()
    palavras_filtradas = []
    
    for palavra in palavras:
        if palavra in denylist_lower:
            palavra_filtrada = '*' * len(palavra)
        else:
            palavra_filtrada = palavra
        palavras_filtradas.append(palavra_filtrada)
    texto_filtrado = ' '.join(palavras_filtradas)
    
    return texto_filtrado

texto = "Eu não gosto de chatgpt."
denylist = ["Eu", "gosto", "chatgpt."]

texto_filtrado = filtrar(texto, denylist)
print(texto_filtrado)
