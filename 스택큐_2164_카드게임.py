# 스택(후입선출) 1 2 3 4의 순서로 있다면
# 4를 버리고 3을 가장 아래인 3 1 2순서로 넣는거
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
Queue = deque()
for i in range(1, n+1) :
    Queue.append(i)


while len(Queue) > 1 :
    Queue.popleft();
    value = Queue.popleft();
    Queue.append(value);

print(Queue[0])


