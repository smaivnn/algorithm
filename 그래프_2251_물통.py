'''
물컵 C의 물을 a, b에 조건에 따라 옮겨 담으면서 a에 물이 비었을 때 c에 담긴 물의 양을 모두 구하는 것


<<아이디어>>
그냥 이해하려고 보고 따라 침
'''
from collections import deque
Sender = [0,0,1,1,2,2]
Receiver = [1,2,0,2,0,1]
now = list(map(int, input().split()))

# 201 인 이유는 범위가 200까지이기 때문
visited = [[False for j in range(201)] for i in range(201)]
answer = [False] * 201


def bfs() :
  queue = deque();
  queue.append((0,0))
  visited[0][0] = True 
  answer[now[2]] = True
  while queue :
    now_Node = queue.popleft()
    A = now_Node[0]
    B = now_Node[1]
    C = now[2] - A - B # C는 A와 B를 뺀 나머지 물의 양
    for k in range(6) :
      next = [A,B,C]
      next[Receiver[k]] += next[Sender[k]] # 1) b = b + a
      next[Sender[k]] = 0 # 1) a = 0
      if next[Receiver[k]] > now[Receiver[k]] : # 1) b가 넘치면
        next[Sender[k]] = next[Receiver[k]] - now[Receiver[k]]
        next[Receiver[k]] = now[Receiver[k]]
      if not visited[next[0]][next[1]] :
        visited[next[0]][next[1]] = True
        queue.append((next[0], next[1]))
        if next[0] == 0 :
          answer[next[2]] = True

bfs();

for i in range(len(answer)) :
  if answer[i] :
    print(i, end=' ')