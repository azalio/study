from collections import Counter

X = int(input())
sizes = input()
sizes = sizes.split()
sizes_counter = dict(Counter(sizes))
num_of_custumers = int(input())
summa = []
for _ in range(num_of_custumers):
    size, price = input().split()
    price = int(price)
    try:
        if sizes_counter[size] > 0:
            summa.append(price)
            sizes_counter[size] -= 1
    except KeyError:
        pass
print(sum(summa))
