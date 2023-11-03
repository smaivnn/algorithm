"""
N개의 동전으로 K원을 만드는 문제

오름차순으로 동전들이 주어진다.

<< 아이디어 >>

0. k원을 만들기 위해서 가장 적게 동전을 사용하려면 가장 큰 동전부터 사용되어야 한다.

1. 따라서 가장 큰 동전부터 몇 개가 k원에 적용되는지 나누어서 확인한다.

2. 이때 나누어 떨어지지 않는다면 다음으로 넘어간다.

3. 위 과정을 반복한다.
"""

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

j = n - 1  # 가장 큰 동전부터 확인
cnt = 0  # 동전의 개수

while k > 0:
    if k >= coins[j]:
        cnt += k // coins[j]
        k %= coins[j]
    else:
        j -= 1

print(cnt)
