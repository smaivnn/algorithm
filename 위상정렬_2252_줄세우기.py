"""
줄 세우기 프로그램

<<아이디어>>
학생 : 노드
비교 : 에지
라고 생각하고, 답이 여러개일 경우 아무거나 출력하라에서 위상정렬을 파악

"""
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]  # 노드 데이터 저장 인접리스트 (1->3, 2->3과 같은 표현)
indegree = [0 for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    indegree[b] += 1  # b의 진입차수 1 증가

# print(arr)
# print(indegree)
queue = deque()

# 진입 차수 리스트의 값이 0인 노드(학생)를 큐에 삽입
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

# print(queue)

while queue:
    now = queue.popleft()
    print(now, end=" ")
    for next in arr[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)
