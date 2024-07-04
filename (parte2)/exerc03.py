def sum_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

def find_amicable_numbers(limit):
    amicable_numbers = []
    for a in range(1, limit):
        b = sum_divisors(a)
        if a != b and sum_divisors(b) == a and b < limit:
            if (b, a) not in amicable_numbers: 
                amicable_numbers.append((a, b))
    return amicable_numbers

def sum_amicable_numbers(limit):
    amicable_pairs = find_amicable_numbers(limit)
    amicable_sum = 0
    for pair in amicable_pairs:
        amicable_sum += pair[0] + pair[1]
    return amicable_sum

limite = 10000
sum_amigos = sum_amicable_numbers(limite)
print("Soma de todos os números amigos menores que 10000:", sum_amigos)
