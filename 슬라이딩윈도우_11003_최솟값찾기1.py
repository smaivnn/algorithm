from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split());
arr = list(map(int, input().split()));
arr_queue = deque();


for i in range(N) :
  while arr_queue and arr_queue[-1][0] > arr[i] :
    arr_queue.pop()
  arr_queue.append((arr[i], i))
  if arr_queue[0][1] <= i-L :
    arr_queue.popleft();
  print(arr_queue[0][0], end= ' ')
