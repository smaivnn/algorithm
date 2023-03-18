import sys
input = sys.stdin.readline

n = int(input());
arr = [0] * n;

for i in range(n) :
    arr[i] = int(input());

for i in range(n) :
    for j in range(n) :
        if arr[i] < arr[j] :
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp;

for i in range(n) :
    print(arr[i])