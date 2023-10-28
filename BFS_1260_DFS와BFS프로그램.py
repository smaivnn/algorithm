import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# DFS
# v부터 시작을 한다.
def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in sorted(graph[v]):
        if not (visited[i]):
            dfs(i)


dfs(v)

visited = [False] * (n + 1)
print()


def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=" ")
        for i in sorted(graph[now]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(v)
