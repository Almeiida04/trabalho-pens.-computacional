def eh_palindromo(s):
    s = s.lower().replace(" ", "")  
    return s == s[::-1]

texto = "SOCORRAM ME EM MARROCOS"
resultado = eh_palindromo(texto)
print(f"A frase '{texto}' é um palíndromo? {resultado}")
