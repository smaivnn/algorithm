# 오름차순으로 정렬을 진행한 후
# 앞에서부터 묶어가며 더해나가면된다.
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = 0;

arr.sort()
value = 0;

for i in range(n):
    ans = ans + arr[i]
    value = value + ans
print(value)

