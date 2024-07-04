def gerar_intervalo_incrementado(n, i):
    
    if i <= 0:
        print("O valor de incremento deve ser maior que 0.")
        return None
    
    intervalo = []
    for num in range(0, n + 1, i):
        intervalo.append(num)
    
    return intervalo

N = 20
incremento = 5
resultado = gerar_intervalo_incrementado(N, incremento)
print(resultado) 
