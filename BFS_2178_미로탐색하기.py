import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]  # 상하좌우

for i in range(n):
    number = list(input())
    for j in range(m):
        graph[i][j] = int(number[j])


# bfs를 실행한다
# 1. 시작점을 큐에 넣는다.
# 2. visited에 시작점을 넣는다.
# 3. 큐가 빌 때까지 반복한다.
# 4. 큐에서 하나를 꺼낸다.
# 5. 그래프의 상하좌우를 확인한다.
# 6. 상하좌우중 1이고, 방문하지 않았다면, 큐에 넣는다.
# 7. 큐에 넣고, 방문했다고 표시한다.
# 8. 몇번만에 도착했는지를 출력한다.
def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x >= 0 and y >= 0 and x < n and y < m:  # 범위를 벗어나지 않는다면
                if graph[x][y] == 1 and not visited[x][y]:
                    queue.append((x, y))
                    visited[x][y] = True
                    graph[x][y] = graph[now[0]][now[1]] + 1  # 이동횟수를 저장한다.


bfs(0, 0)
print(graph[n - 1][m - 1])
