a, b, c, d = input().split()

h = int(a)
b = int(b)
c = int(c)
s = int(d)

print('%.1f MB' % (h*b*c*s/8/1024/1024))
