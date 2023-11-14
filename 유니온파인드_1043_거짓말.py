"""
거짓말을 할 수 있는 파티의 최대 갯수 구하기
조건1) 모든 파티에 참가해야한다.
조건2) 진실을 아는 사람이 있는 파티에 참가하면 거짓말을 할 수 없다.
조건3) 다른 파티에서 진실을 들은 사람이 있다면, 그 사람은 진실을 알게되어 거짓말을 할 수 없다.


<<아이디어>>
서로 다른 집합을 사용하므로 유니온 파인드를 사용한다.
파티 안에 인원들에 대해서 

예제5)로 파악하기
10 9
4 1 2 3 4
2 1 5 (1,5 한 집합으로 union)
2 2 6 (2,6 한 집합으로 union)
1 7 ...
1 8 ...
2 7 8 ...
1 9 ...
1 10 ...
2 3 10 (3,10 한 집합으로 union)
1 4 ...

파티가 진행됨에 따라 union을 진행하면 각 파티별로 집합이 나뉘게 된다. 

진실을 아는 집합의 인덱스와 같지 않은 파티의 갯수를 구하면 된다.


<<의사코드>>
n: 사람의 수, m : 파티의 수 입력
truth 진실을 아는 사람의 수, 진실을 아는 사람 입력

def union
def find

party = 파티번호와 파티에 참가하는 사람들의 집합

for 파티 수만큼
  for 파티에 참가하는 인원만큼
    union

for 파티 수만큼
  for 진실을 아는 사람 만큼
    if 파티에 참가한 0번 사람(대표) == 진실을 아는 사람
      break
    else
      count += 1
"""


import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
truth = list(map(int, input().split()))  # [0] : 아는 사람의 수
parent = [i for i in range(n + 1)]  # 사람
count = 0


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


party = []
for i in range(m):
    party.append(list(map(int, input().split())))

for i in range(m):
    for j in range(party[i][0]):
        # print(f"횟수 : {party[i][0]} union {party[i][1]} {party[i][j+1]}")
        union(party[i][1], party[i][j + 1])

for i in range(m):
    isSame = True
    for j in range(truth[0]):
        mainNum = find(party[i][1])
        if mainNum == find(truth[j + 1]):
            isSame = False
            break
    if isSame:
        count += 1


print(count)
