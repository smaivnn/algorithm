import sys
input = sys.stdin.readline

n = int(input());
arr = [0] * n;

for i in range(n) :
    arr[i] = int(input());
swap = 0
for i in range(n-1) :
    for j in range(n-1-i) :
        if arr[j] > arr[j+1] :
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp;
            swap += 1

for i in range(n) :
    print(arr[i])

print(swap)