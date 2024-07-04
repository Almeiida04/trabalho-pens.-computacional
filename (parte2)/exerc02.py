def obter_numeros_paridade(N, c):
    numeros = []
    for num in range(1, N):
        if c == 'p' and num % 2 == 0:
            numeros.append(num)
        elif c == 'i' and num % 2 != 0:
            numeros.append(num)
    return numeros

N = 15
caractere = 'i'
resultado = obter_numeros_paridade(N, caractere)
print("Números", caractere, "no intervalo de 1 até", N - 1, ":", resultado)
