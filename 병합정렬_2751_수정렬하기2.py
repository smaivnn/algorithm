import sys
input = sys.stdin.readline

# 재귀를 이용해서 최소단위로 쪼갠다.
# if 리스트의 크기가 1보다 크면 
# 재귀함수를 다시 들어간다, mergeSort(start, middle),mergeSort(middle, end)
# 최소값을 찾는 로직.
def mergeSort(array) :
    # 재귀
    if len(array) <= 1 :
        return array;

    mid = len(array) // 2;
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    # 합치기
    i,j,k = 0,0,0

    while i < len(left) and j < len(right) :
        if left[i] < right[j] : 
            array[k] = left[i]
            i += 1
        else :
            array[k] = right[j]
            j += 1
        k += 1
    
    # 나머지 처리
    if i == len(left) :
        while j < len(right) :
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right) :
        while i < len(left) :
            array[k] = left[i]
            i += 1
            k += 1
    return array;



N = int(input())
arr = [0] * N
for i in range(N) :
    arr[i] = int(input());


temp = mergeSort(arr)

for i in temp :
    print(F"{i}")