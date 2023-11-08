'''
두 수의 최대 공약수를 구하고 그 수만큼 1을 출력하면 된다.

<< 아이디어 >>
유클리드 호제법으로 최대 공약수를 구한다.

<< 의사코드 >>
n, m = 입력받는다

def gcd(a, b)
    if b가 0이라면
        return a
    return gcd(b, a % b)

gcd_value = gcd(n, m)
for i in range(gcd_value)
    print(1)

'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

gcd_value = gcd(n, m)
for i in range(gcd_value):
    print(1, end='')