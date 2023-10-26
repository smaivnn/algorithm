# N개의 수를 정렬하고 앞에서부터 K번째 수를 출력하는 문제.
# 나중에 다른 정렬 알고리즘으로 풀어보기
import sys
input = sys.stdin.readline

# 피벗을 설정하는 역할을 한다. 
# 피벗을 기준으로 왼쪽에는 피벗보다 작은 값이 오고, 오른쪽에는 피벗보다 큰 값이 오도록 한다.
def partition(left, right) :
    global arr
    pivot = arr[right]
    i = left - 1

    for j in range(left, right) :
        if arr[j] < pivot :
            i += 1
            swap(i, j)

    swap(i+1, right)
    return i+1


def swap(i, j) :
    global arr
    temp = arr[i]
    arr[i] = arr[j] 
    arr[j] = temp 

def quickSort(left, right) :
    global arr
    if left < right :
        pivot = partition(left, right)
        if pivot == k-1 :
            return 
        quickSort(left, pivot-1)
        quickSort(pivot+1, right)
    

n, k = map(int, input().split())
arr = list(map(int, input().split()))

quickSort(0, n-1)

print(f"{arr[k-1]} ")
