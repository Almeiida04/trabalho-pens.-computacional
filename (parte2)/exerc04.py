def calcula_h(n):
    h = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            h -= 1 / i
        else:
            h += 1 / i
    return h

N = 10  
resultado = calcula_h(N)
print(f"O valor de H para N = {N} é aproximadamente {resultado:.6f}")
