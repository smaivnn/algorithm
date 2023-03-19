import sys
input = sys.stdin.readline
print = sys.stdout.write

arr = list(input());

for i in range(len(arr)-1) :
    maxValue = i;
    for j in range(i+1, len(arr)-1) :
        if arr[j] > arr[maxValue] :
            maxValue = j
    temp = arr[i]
    arr[i] = arr[maxValue]
    arr[maxValue] = temp

for i in range(len(arr)-1) :
  print(f"{arr[i]}")
            