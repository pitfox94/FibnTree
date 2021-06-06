# Implementa la función fib(n) que retorna el n-ésimo número de la serie
# de Fibonacci:
# fib(1) = 1
# fib(2) = 1
# fib(n) = fib(n - 1) + fib(n - 2), para todo n > 2.


def fib(n):
    global numbers
    numbers = []
    anterior, actual = (0, 1)
    for i in range(2, n+1):
        anterior, actual = (actual, anterior + actual)
        numbers.append(actual)
    return actual
    


if __name__ == "__main__":
    # Prueba de la función: imprime los primeros 10 números en una línea
    # separados por coma y espacio.
    fib(10)
    prueba_fib = ', '.join(map(str,numbers[0:10]))
    print(prueba_fib)
