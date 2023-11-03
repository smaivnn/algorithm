"""
수열 내에서 2개씩 묶어서 수열의 최댓값을 구하는 문제

<< 아이디어 >>
수열의 최댓값을 구하려면 가장 큰 수끼리 곱해야한다.
또한 음수의 경우도 존재하므로 음수는 가장 작은 음수끼리 곱해야한다.
정렬된 수를 사용하기에 우선순위 큐를 사용한다.

우선순위 큐는 오름차순으로 정렬되어있으므로 양수, 음수 부분을 나누어서 정렬한다.

<< 의사코드 >>
n입력
수열 입력
sum, zero

우선순위 큐 사용

하나씩 뺴면서 두개씩 묶어서 곱한다.
만약 0보다 큰 값이 1개 남는다면 해당 값을 더한다.
0이 남는다면 음수 부분을 정렬한다.
마찬가지로 가장 작은값을 두개씩 묶어서 곱한다.
하나가 남는다면 0과 곱한다. 그것이 아니라면 더한다.
"""

import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
plus_queue = PriorityQueue()
minus_queue = PriorityQueue()
sum = 0
zero = 0

for _ in range(n):
    num = int(input())
    if num > 0:
        plus_queue.put((-1 * num, num))
    elif num == 0:
        zero += 1
    else:
        minus_queue.put(num)

while plus_queue.qsize() > 0:
    # 1개가 남았다면 해당 값을 더한다.
    if plus_queue.qsize() == 1:
        sum += plus_queue.get()[1]
        break

    a = plus_queue.get()[1]
    b = plus_queue.get()[1]
    # 1이 나온다면 둘 모두를 더하는 것이 더 큰 값이다.
    if a == 1 or b == 1:
        sum += a + b
    else:
        sum += a * b


while minus_queue.qsize() > 0:
    # 1개가 남았다면 0이 몇개 있는지 확인한다. 0이 있다면 0과 곱한다. 0이 없다면 더한다.
    if minus_queue.qsize() == 1:
        if zero > 0:
            sum += 0
        else:
            sum += minus_queue.get()
        break

    a = minus_queue.get()
    b = minus_queue.get()
    sum += a * b


print(sum)
