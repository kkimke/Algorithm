a = input()
a = int(a)

n = 0

for i in range(1, a + 1):
    if (i % 2 == 0):
        n += i

print(n)
