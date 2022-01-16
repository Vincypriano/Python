def acrescenta_1(lista = []):
    lista.append(1)
    return lista

print(acrescenta_1(), acrescenta_1())

números_do_vini = [1, 2, 3]
números_da_ju = números_do_vini.copy()

números_da_ju.append(4)
print(f"Números escolhidos pela Ju: {números_da_ju}")
print(f"Números escolhidos pelo Vini: {números_do_vini}")

def acrescenta_1_sem_padrão_mutável(lista = None):
    if lista is None:
        lista = []
    lista.append(1)
    return lista
print(acrescenta_1_sem_padrão_mutável(), acrescenta_1_sem_padrão_mutável())

def enésimo_elemento_fibonacci(n, fibonacci_cached={0:0, 1:1}):
    if n not in fibonacci_cached:
        fibonacci_cached[n] = (
            enésimo_elemento_fibonacci(n - 1) + enésimo_elemento_fibonacci(n - 2)
        )
    return fibonacci_cached[n]

print(enésimo_elemento_fibonacci(10))