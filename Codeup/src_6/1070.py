a = input()
a = int(a)

if a == 1 or a == 2 or a == 12:
    print('winter')
elif a <= 5 and a >= 3:
    print('spring')
elif a <= 8 and a >= 6:
    print('summer')
else:
    print('fall')
