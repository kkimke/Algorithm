a, b = input().split()
a = int(a)
b = int(b)

print(a | b)
'''
python 비트단위 연산자(bitwise) 중 or
- 표기: |
- 둘 중 하나라도 1인 자리를 1로 만들어준다

32비트 2진수 예시
3     : 00000000 00000000 00000000 00000011
5     : 00000000 00000000 00000000 00000101
3 | 5 : 00000000 00000000 00000000 00000111
'''
