def bubble_sort(values, reverse):
    n = len(values)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (values[j] > values[j + 1]) if reverse else (values[j] < values[j + 1]):
                values[j], values[j + 1] = values[j + 1], values[j]
    return values

valores = [5.6, 2.3, 1.8, 4.1, 3.7]
ordenado_decrescente = bubble_sort(valores, reverse=True)
print("Valores ordenados (decrescente):", ordenado_decrescente)
