a, b = input().split()
a = int(a)
b = int(b)

print(a & b)

'''
python 비트단위 연산자(bitwise) 중 and
- 표기: &
- 대응하는 비트가 모두 1이면 1을 반환

32비트 2진수 예시
3     : 00000000 00000000 00000000 00000011
5     : 00000000 00000000 00000000 00000101
3 & 5 : 00000000 00000000 00000000 00000001
'''
