from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write # 개행제거

n = int(input())
# 우선순위 큐 만들기
queue = PriorityQueue();

# 큐만큼 반복한다
# 값을 받는다
# 만약 0이라면 큐에서 get한다
for i in range(n) :
    num = int(input())
    if num == 0 :
        # 큐에 남은게 없다면 0을 출력한다.
        if queue.empty() :
            print('0\n')
        # 큐 요소를 get한다.
        else :
            temp = str(queue.get())
            print(temp[1]+'\n')
    else :
        # (절댓값을 기준으로, 만약 같다면 음수를 우선)
        # 기본적으로 오름차순임
        queue.put((abs(num), num)) 
