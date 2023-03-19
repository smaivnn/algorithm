# 오름차순으로 정렬을 진행한 후
# 앞에서부터 묶어가며 더해나가면된다.
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = 0;

for i in range(1, len(arr)) :
    minIdx = i
    for j in range(i) :
        if arr[minIdx] < arr[j] :
            value = arr[minIdx]
            arr[j + 1 : i + 1] = arr[j : i]
            arr[j] = value


for i in range(len(arr)) : 
    for j in range(i+1) :
        ans = ans + arr[j]

# print(arr)

print(ans)