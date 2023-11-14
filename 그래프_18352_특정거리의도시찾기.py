"""
문제 : 
x에서 출발하여 정확히 k거리에 있는 노드를 찾는 문제 (최단거리 찾기)

<< 아이디어 >>
최단거리 문제이기에 bfs를 이용한다.
이동 거리가 무조건 1이므로 이동거리를 저장한다.
마지막에 k와 같은 거리를 가진 노드를 출력한다.

<< 의사코드 >>
n, m, k, x를 입력받는다.
graph = 인접 그래프를 생성한다.
visited = 방문 여부를 확인하는 배열을 생성한다.
queue = deque()를 생성한다.
distance = 거리를 저장하는 배열을 생성한다.



def bfs(x):
    queue에 x를 넣는다.
    visited[x] = True
    distance[x] = 0
    while queue가 비어있지 않은 동안:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue에 i를 넣는다.
                visited[i] = True
                distance[i] = distance[now] + 1

                
인접그래프를 입력받는다.
bfs(x)를 호출한다.
for i in range(1, n + 1):
  if distance[i] == k:
    i를 출력한다.
"""

from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
queue = deque()
distance = [0] * (n + 1)


def bfs(x):
    queue.append(x)
    visited[x] = True
    distance[x] = 0
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[now] + 1


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(x)
# print(distance)
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
if k not in distance:
    print(-1)
