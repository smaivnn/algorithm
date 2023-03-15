# x가 아닌 정수를 배열에 넣는다.
# 0이 입력될경우 절댓값이 가장 작은 수 부터 출력한다.
# 만약 절댓값이 같은 값이 여러개라면, 원래 값이 작은 것부터 출력한다.

# 문제 해결
# 우선순위 큐를 생성한다.
# 입력된 N횟수만큼 배열에 값을 넣는다.
# 이 때 넣을때 절댓값abs(값)을 확인한 후 더 작은값부터 우선순위를 부여해서 넣는다.

from queue import PriorityQueue
import sys
input = sys.stdin.readline
# 개행제거
print = sys.stdout.write

N = int(input())
# 우선순위 큐 만들기
Queue = PriorityQueue();

for i in range(N) :
    value = int(input())
    if value == 0 :
        if Queue.empty() :
            print("0\n")
        else : 
            temp = Queue.get();
            print(f"{str(temp[1])}\n")
    else :
        # put의 원리 : 우선순위 큐의 데아터 추가시 우선순위는 
        # 정렬 우선순위가 기준이 된다.
        # 따라서 abs를 먼저 우선 정렬을 하고, 이후에 value값으로 다시 정렬한다.
        # 따라서 절댓값이 같다면 양수,음수를 판별하는 것이다.
        Queue.put((abs(value), value))

