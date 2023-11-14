"""
계획대로 여행이 가능한지 판별하는 문제.
판별하는 방법 : 
같은 집합에 있다면 여행이 가능하다. 
같은 집합 -> 이동 경로로 표시된 그래프들이 모두 연결되어있다 

<< 의사코드 >>
n입력
m입력
def find
def union

for
  parent[i] = i

for i
  for j
    입력받으며 유니온 실행

route 입력
for
  route find실행

route 0,1,2가 모두 같다면
yes출력
아니면
no출력
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())  # 도시의 수
m = int(input())  # 여행 계획에 속한 도시들의 수
parent = [i for i in range(n + 1)]


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


for i in range(0, n + 1):
    parent[i] = i
for i in range(n):
    dosi = list(map(int, input().split()))
    for j in range(n):
        if dosi[j] == 1:
            union(i + 1, j + 1)

route = list(map(int, input().split()))


# route의 도시가 모두 같은 집합이라면 -> parent[route]가 모두 같다면
isConneted = True
value = parent[route[0]]
for i in range(1, len(route)):  # 0 1 2
    if parent[route[i]] != value:
        # if value != find(route[i]):
        isConneted = False
        break

if isConneted:
    print("YES")
else:
    print("NO")
