"""
두 수의 최소공배수를 구하는 문제

<< 아이디어 >>
최소공배수를 구하는 법은 두 수의 곱을 최대공약수로 나누면 된다.
최소 공약수를 구하는 법 : 유클리드 호제법
유클리드 호제법은 두수 중 큰 수를 작은수로 나누고 나머지가 0이 아니면 작은수를 큰 수로, 나온 값을 작은수로 하여 나머지가 0이 될 때까지 반복한다.
그러면 나머지가 0이 되었을 때의 작은 수가 최대공약수가 된다.

<< 의사코드 >>
n을 입력받는다

def gcd(a, b)
    if b가 0이라면
        return a
    return gcd(b, a % b)

for n번 만큼
  a, b를 입력받는다
  if b가 a보다 크다면
    a, b = b, a 
  gcd_value = gcd(a, b)
  print(a * b // gcd_value)

"""
import sys

input = sys.stdin.readline

n = int(input())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in range(n):
    a, b = map(int, input().split())
    if b > a:
        a, b = b, a
    gcd_value = gcd(a, b)
    print(a * b // gcd_value)
