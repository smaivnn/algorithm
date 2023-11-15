"""
<<아이디어>>
인접리스트를 생성한다.
1 : 2, 3, 4
2 : 
3 : 4, 5 
4 :
5 :

이때 진입차수는 
1 2 3 4 5 < 인덱스
0 1 1 2 1 < 진입차수
가 된다.

큐에 0인 값을 넣고 위상 정렬을 실행한다.

값 1일 때, 2,3,4의 진입차수를 1씩 감소시킨다.
그리고 2,3,4를 확인하는데, 이 때 이들의 buildingTime를 상승시킨다.
이렇게 상승한 buildingTime은 1(now)에서 2,3,4(next)를 거친 시간이라는 뜻이다.
따라서 진입차수가 2이상인 것은 이미 어떠한 것을 하나 거쳐왔다는 뜻이 된다.
또한 여러개의 건물을 동시에 지을 수 있다.

따라서 (현재 들어있는 값, 지금 노드에게 뻗은 값의 총량 (buildingTime[now] + now노드의 값))을 비교하여 더 큰 값을 넣어준다.

"""
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

arr = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
buildingTime = [0 for _ in range(n + 1)]

# 인접 리스트 생성
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    buildingTime[i] = data[0]
    for j in range(1, len(data) - 1):
        arr[data[j]].append(i)
        indegree[i] += 1

queue = deque()

# 진입 차수 리스트의 값이 0인 노드를 큐에 삽입
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

result = [0 for _ in range(n + 1)]

# 위상정렬 실행
while queue:
    now = queue.popleft()
    for next in arr[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)
        result[next] = max(result[next], result[now] + buildingTime[now])

for i in range(1, n + 1):
    print(result[i] + buildingTime[i])
