def ePrimo(n):
    if n <= 1:
        return 'Numero não é primo'

    for i in range(2, n//2):
        if n % i == 0:
            return 'Numero não é primo'

    return 'Numero é primo'

num = int(input('Digite um número: '))
res = ePrimo(num)
print(f'{num} é primo? {res}')