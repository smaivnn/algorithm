"""
범위 내에서 소수의 N제곱의 갯수를 구하는 문제

예를 들어 1 ~ 10 이라면
소수 : 2,3,5,7
2의 N제곱 : 2, 4, 8
3의 N제곱 : 3, 9
4의 N제곱 : 4
이때 N>=2이므로 2, 3, 4의 N제곱의 갯수는 3개이다.

<< 아이디어 >>
먼저 1~10까지의 소수를 구한다.
그리고 그 소수들의 N제곱을 구한다.
그리고 그 N제곱들의 갯수를 구한다.

<< 의사코드 >>
count = 0
a, b를 입력받는다
for i in range(2, b+1)
  1~b까지의 배열을 만든다

for i in range(2, b+1)
  소수가 아니라면 넘어간다
  if 소수라면
    for
      소수의 배수를 모두 지운다

# 범위 내 소수의 제곱이 몇개 있는지 구한다.
for i in range(2, b+1)
  if 남아있는 소수하면
    while i의 제곱이 b보다 작거나 같다면
      count += 1
"""

import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split())
arr = [i for i in range(b + 1)]
count = 0

for i in range(2, int(math.sqrt(len(arr))) + 1):
    # 소수가 아니라면 넘어간다
    if arr[i] == 0:
        continue
    # 소수라면 그 소수의 배수를 모두 지운다
    for j in range(i + i, b + 1, i):
        arr[j] = 0

for i in range(2, b + 1):
    if arr[i] != 0:
        j = i * i
        while j <= b:
            if j >= a:
                count += 1
            j = j * i

print(count)
"""
정답 코드, 위의 코드는 동작하나 메모리 초과가 났다.

import math

Min, Max = map(int, input().split())
A = [0] * (10000001)

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)) + 1)):
    if A[i] == 0:
        continue
    for j in range(i + i, len(A), i):
        A[j] = 0

count = 0
for i in range(2, 10000001):
    if A[i] != 0:
        temp = A[i]
        while A[i] <= Max / temp:
            if A[i] >= Min / temp:
                count += 1
            temp *= A[i]

print(count)
"""
