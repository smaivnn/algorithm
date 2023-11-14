"""
가장 많은 해킹이 일어나도록 하는 문제

<< 아이디어 >>
Q. 가장 많은 해킹이 일어나려면?
A. 가장 신뢰를 많이 받는 컴퓨터를 찾아야 한다.

bfs등 dfs든 일단 모든 노드를 탐색하며 각 노드의 신뢰도를 향상시켜 준다.

<< 의사코드 >>
n,m을 입력받는다.
graph = 인접 그래프를 생성한다.(n+1만큼)
visited = 방문 여부를 확인하는 배열을 생성한다.
queue = deque()를 생성한다.
result = 결과를 저장하는 배열을 생성한다.

def bfs(x):
    queue에 x를 넣는다.
    visited[x] = True
    while queue가 비어있지 않은 동안:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue에 i를 넣는다.
                visited[i] = True
                result[i] += 1


for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

모든 노드에 대해서 bfs를 실행한다.
그 이유는 모든 노드에 대해서 신뢰도를 향상시켜야 하기 때문이다.

가장 큰값을 순서대로 출력한다.
"""
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = [0] * (n + 1)


def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result[i] += 1


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    bfs(i)

max_value = max(result)

for i in range(1, n + 1):
    if result[i] == max_value:
        print(i, end=" ")
