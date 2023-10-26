import sys
input = sys.stdin.readline
result = 0;

def mergeSort(start, end) :
    if start < end :
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid+1, end)
        merge(start, mid, end)

def merge(start, mid, end) :
    global arr
    global answer
    global result
    i = start
    j = mid + 1
    k = start

    while i <= mid and j <= end :
        if arr[i] <= arr[j] :
            answer[k] = arr[i]
            i += 1
        else :
            answer[k] = arr[j]
            result = result + (j - k)
            j += 1
        k += 1

    if i > mid :
        for t in range(j, end+1) :
            answer[k] = arr[t]
            k += 1
    else :
        for t in range(i, mid+1) :
            answer[k] = arr[t]
            k += 1

    for t in range(start, end+1) :
        arr[t] = answer[t]


N = int(input())
arr = list(map(int, input().split()))


answer = [0] * N;

mergeSort(0, N-1)

print(f"{result}")
