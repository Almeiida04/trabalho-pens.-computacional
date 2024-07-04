def imprime_gradual(s):
    n = len(s)
    
    if n % 2 == 0:
        print("A palavra deve ter um número ímpar de caracteres.")
        return
    
    for i in range(n):
        print(s[:i+1])

palavra = "SONHO"
imprime_gradual(palavra)
