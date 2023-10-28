import sys
from collections import deque

input = sys.stdin.readline


n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distances = [0] * (n + 1)


for _ in range(n):
    numArr = list(map(int, input().split()))
    for i in range(1, len(numArr), 2):
        if i + 1 == len(numArr):
            break
        graph[numArr[0]].append((numArr[i], numArr[i + 1]))


# 임의의 한 노드를 선택했을 때 가장 먼 노드는 무조건 지름의 한 끝점이다. (가장 긴 것이 포함되어야 하기 때문)
# 따라서 bfs를 진행한 후 가장 먼 노드를 찾고, 그 노드에서 다시 bfs를 진행하면 지름을 구할 수 있다.
# 가장 먼 노드는 어떻게 구할까?
# bfs를 진행한 후 각 노드의 거리를 저장한 배열을 만들어서 가장 큰 값을 찾으면 된다.
def bfs(v):
    queue = deque([v])  # v = 3
    visited[v] = True
    while queue:
        now = queue.popleft()  # now = 3
        for i in graph[now]:  # i = (1,2), (4,3)
            if not visited[i[0]]:
                queue.append(i[0])
                visited[i[0]] = True
                distances[i[0]] = distances[now] + i[1]  # 3: 2


bfs(2)

maxDistance = max(distances)
# 가장 거리가(index)가 큰 노드를 찾는다.
for i in range(len(distances)):
    if distances[i] == maxDistance:
        start = i
        break

# 다시 bfs를 진행한다.
visited = [False] * (n + 1)
distances = [0] * (n + 1)

bfs(start)
print(max(distances))
