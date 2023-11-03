"""
카드 묶은에서 2개씩 선택해서 최소 비용으로 합치기

<< 아이디어 >>
최소 비용으로 합치려면 카드 묶음을 작은것부터 선택해서 합쳐야 한다.

두 개의 데이터를 선택해야 하고, 이 선택된 것을 또 합쳐주어야 한다.
10 20 40일 때
10, 20을 합치며 30번의 연산이, 그리고 이 30과 40을 합치며 70번의 연산이 필요하다. 즉 100의 연산이 필요한데, 이렇게 앞선 연산들이 또 연산의 대상이 발생하므로 배열보다는 우선순위 큐를 사용하는 것이 편하다.

<< 의사코드 >>
n입력
우선순위 큐

우선순위큐가 빌때까지 -> 한개 남을 때까지 (마지막으로 합쳐진것이 남아 더이상 합쳐질 것이 없을 때까지)
    가장 작은 두개의 수를 뽑아서 합친다. (sum)
    그 합을 우선순위 큐에 넣는다.

sum출력



"""

import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
queue = PriorityQueue()

for _ in range(n):
    queue.put(int(input()))

sum = 0

while queue.qsize() > 1:
    a = queue.get()
    b = queue.get()
    sum += a + b
    queue.put(a + b)

print(sum)
