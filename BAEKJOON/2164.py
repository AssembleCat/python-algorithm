n = int(input())

if n == 1:
    print(1)

for i in range(20):
    if 2 ** i < n <= 2 ** (i + 1):
        print((n - (2 ** i)) * 2)
