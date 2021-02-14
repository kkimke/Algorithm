value = input()

value_chr = ord(value)
a = ord('a')

while a <= value_chr:
    print(chr(a), end=' ')
    a += 1
