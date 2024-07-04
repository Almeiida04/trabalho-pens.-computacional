import math

def fibo(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def soma(seq):
    return sum(seq)

def avg(seq):
    return sum(seq) / len(seq)

def stddev(seq):
    if len(seq) <= 1:
        return 0.0
    mean = avg(seq)
    variance = sum((x - mean) ** 2 for x in seq) / len(seq)
    return math.sqrt(variance)

fib = fibo(10)
print("Sequência de Fibonacci:", fib)
print("Soma da sequência:", soma(fib))
print("Média da sequência:", avg(fib))
print("Desvio padrão da sequência:", stddev(fib))
