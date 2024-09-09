"""
임계 경로의 시간과, 해당 경로 상 있는 도로의 수를 구하는 문제.

<<아이디어>>
1. 사람들이 출발 도시에서 도착 도시까지 갔을 때 만나는 시간은 임계 경로일 때이다. 즉, 가장 시간이 길 때이다.

2. 모든 도시가 일방향, 사이클이 없다. 위상정렬을 이용해서 시작부터 도착 도시까지의 최장 거리를 구할 수 있다. 

3. 구한 이후, 도로의 갯수를 구해야 한다. 도로의 갯수는 출발->도착 도시를 반대로 도착->출발로 다시한번 진행해본다.
이때 이미 구해져 임계 경로 리스트를 바탕으로 구하면 된다.

4. 
인접 리스트        역방향 리스트

1    2 3 4        1    
2    6 7          2    1
3    5            3    1
4    6            4    1
5    6            5    3
6    7            6    2 4 5
7                 7    2 6

정방향 진입 차수는 다음과 같다.
1 2 3 4 5 6 7 인덱스
0 1 1 1 1 3 2 값

위를 바탕으로 임계 경로를 구하면 다음과 같다.
이 때 임계 경로는 max(임계경로[next], 임계경로[now] + now에서 next값)이다.

시작도시1, 도착도시7일 때
임계 경로
1 2 3 4 5 6 7 인덱스
0 4 2 3 3 7 12 값

임계경로 : 12

이제 역방향으로 진행한다.

시작도시7, 도착도시1일 때
역방향 진입 차수
1 2 3 4 5 6 7 인덱스
3 2 1 1 1 1 0 값

도시 확인
현재 도시의 정방향 임계 경로 == 다음 도시의 임계 경로 + 현재->다음도시의 경로
7로 예를 들면, 12 == 7 + 5이므로 7->6 도로가 카운트 되며, 큐에 6을 추가한다.

<<의사코드>>
n입력
m입력
정방향 인접리스트
역방향 인접리스트
진입 차수 리스트

for m만큼
  node1(출발노드), node2(도착노드), time(소요시간) 입력
  정방향 인접리스트[node1].append((node2, time))
  역방향 인접리스트[node2].append((node1, time))
  진입 차수 리스트[node2] += 1

queue = deque()

큐에 시작 도시를 넣는다.
임계 경로 리스트
while queue:
  now = queue.popleft()
  for next in 정방향 인접리스트[now]:
    진입 차수 리스트[next[0]] -= 1
    임계 경로 리스트[next] = max(임계 경로 리스트[next], 임계 경로 리스트[now] + next[1])
    if 진입 차수 리스트[next[0]] == 0:
      queue.append(next[0])
  
임계 경로 출력
도로 갯수 = 0
큐 초기화
진입차수 초기화

큐에 도착 도시를 넣는다.
while queue:
  now = queue.popleft() # now = 7
  for next in 역방향 인접 리스트[now] : next # (6,time5)
    if 임계경로 리스트[now] == 임계경로 리스트[next[0]] + next[1]:
      도로 갯수 += 1
      queue.append(next[0])

도로 갯수 출력

"""

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n + 1)]
arr_reverse = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]

for i in range(m):
    node1, node2, time = map(int, input().split())
    arr[node1].append((node2, time))
    arr_reverse[node2].append((node1, time))
    indegree[node2] += 1

queue = deque()

start, end = map(int, input().split())
queue.append(start)

criticalPath = [0 for _ in range(n + 1)]
while queue:
    now = queue.popleft()
    for next in arr[now]:
        indegree[next[0]] -= 1
        criticalPath[next[0]] = max(criticalPath[next[0]], criticalPath[now] + next[1])
        if indegree[next[0]] == 0:
            queue.append(next[0])

print(criticalPath[end])  # 답 1

roadCount = 0
queue.clear()
indegree = [0 for _ in range(n + 1)]
isVisited = [
    False for _ in range(n + 1)
]  # 역경로 중복을 방지해야함. https://www.acmicpc.net/board/view/69771
queue.append(end)
while queue:
    now = queue.popleft()
    for next in arr_reverse[now]:
        if criticalPath[now] == criticalPath[next[0]] + next[1]:
            roadCount += 1
            if not isVisited[next[0]]:
                isVisited[next[0]] = True
                queue.append(next[0])


print(roadCount)  # 답 2
