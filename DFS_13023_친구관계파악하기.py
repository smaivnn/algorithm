import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [False] * (n)


for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, depth):
    visited[v] = True
    if depth == 5:
        print(1)
        exit()
    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth + 1)
    # 재귀가 끝나면 방문처리를 해제해준다
    visited[v] = False


# 그래프의 인덱스 별로 dfs 실행
for i in range(n):
    if not visited[i]:
        dfs(i, 1)
print(0)
