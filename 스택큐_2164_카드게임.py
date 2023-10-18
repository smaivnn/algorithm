# 스택(후입선출) 1 2 3 4의 순서로 있다면
# 1을 버리고 2를 밑으로 넣는것. 1 2 3 4 -> 3 4 2
# 마지막에 남은거 구하기.
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

# 큐에 다 넣는다
# 하나를 버리고, 하나는 반대쪽에 넣는 것을 한다.
# 하나 남을때 까지 반복한다.
for i in range(1, n+1) :
  queue.append(i)

while len(queue) > 1 :
  queue.popleft()
  queue.append(queue.popleft())

print(queue[0])


