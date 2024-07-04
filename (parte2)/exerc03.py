def filtra_numeros(numeros):
    numeros_filtrados = []
    for num in numeros:
        a = num // 100
        b = num % 100
       
        soma = a + b
        quadrado = soma ** 2
       
        if quadrado == num:
            numeros_filtrados.append(num)
    return numeros_filtrados


numeros_originais = [3025, 1234, 9876, 5555]
numeros_filtrados = filtra_numeros(numeros_originais)
print("Números que satisfazem a propriedade:", numeros_filtrados)
