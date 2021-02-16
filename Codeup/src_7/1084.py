a, b, c = input().split()

r = int(a)
g = int(b)
b = int(c)

c = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            c += 1
            print(i, j, k)

print(c)
