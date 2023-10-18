import sys
input = sys.stdin.readline;

"""""
N = int(input());
arr = list(map(int, input().split()));
arr.sort();
count = 0;

for i in range(N) :
    s_idx = 0;
    e_idx = N - 1;
    while s_idx < e_idx :
        if arr[s_idx] + arr[e_idx] == arr[i] :
            if s_idx != i  and e_idx != i :
                count += 1;
                break;
            # case 0 0 0일 때를 고려해야 한다. 나는 제외 되어야 함.
            if s_idx == i :
                s_idx += 1;
            if e_idx == i :
               e_idx -= 1;
        elif arr[s_idx] + arr[e_idx] > arr[i] :
            e_idx -= 1;
        else :
            s_idx += 1;

print(count);
"""""

n = int(input())
arr = list(map(int, input().split()))
value = 0;
start, end = 0, n-1
count = 0;
arr.sort();

while value < len(arr) :
    sum = arr[start] + arr[end]
    if start >= end :
        value += 1
        start = 0;
        end = n-1;
        continue

    if arr[value] > sum :
        start += 1;
    
    elif arr[value] == sum :    
        if start != value and end != value:
            count += 1;
            value += 1;
            start = 0;
            end = n-1
        elif start == value :
            start += 1
        elif end == value :    
            end -=1
    else :
        end -= 1

print(count)
