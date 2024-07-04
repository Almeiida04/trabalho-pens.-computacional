def trocar_elementos(vet):
    n = len(vet)
    for i in range(n // 2):
        vet[i], vet[n - i - 1] = vet[n - i - 1], vet[i]
    return vet

vetor_original = [1, 2, 3, 4, 5, 6]
vetor_trocado = trocar_elementos(vetor_original)
print("Vetor após a troca:", vetor_trocado)
