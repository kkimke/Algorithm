y, m, d = input().split('.')

print('%04d' % int(y), end='.')
print('%02d' % int(m), end='.')
print('%02d' % int(d))


'''
zfill 함수를 이용한다면

y, m, d = input().split('.')
print(y.zfill(4), m.zfill(2), d.zfill(2), sep = '.')
'''
