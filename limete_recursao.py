# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.h


# sys.setrecursionlimit(1004)
def factorial(n):
    if n <=1:
        return 1
    return n * factorial(n - 1)
print('Fatorial 5')
print(factorial(5))
print('Fatorial 10')
print(factorial(10))
print('Fatorial 100')
print(factorial(100))
print('Fatorial 1000')
print(factorial(1000))