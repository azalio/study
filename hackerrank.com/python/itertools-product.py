from itertools import product

a = input()
b = input()
a = a.split()
b = b.split()
a = list(map(int, a))
b = list(map(int, b))
result = list(product(a, b))
print(*result)
