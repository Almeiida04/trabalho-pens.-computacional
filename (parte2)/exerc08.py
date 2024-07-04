def intercala(s1, s2):
    s3 = "".join(c1 + c2 for c1, c2 in zip(s1, s2))
    return s3

string1 = "Quarta"
string2 = "Segunda"
resultado_intercalado = intercala(string1, string2)
print("String intercalada:", resultado_intercalado)

def desintercala(s3, s2):
    s1 = "".join(c1 for c1, c2 in zip(s3, s2))
    return s1

string3 = resultado_intercalado
resultado_desintercalado = desintercala(string3, string2)
print("String desintercalada:", resultado_desintercalado)
