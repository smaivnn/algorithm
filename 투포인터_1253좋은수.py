import sys
input = sys.stdin.readline;

# 변수들을 초기화 한다. 수의 개수 N, 예시 수 배열 arr,
# 좋은 수 파악 count, 시작 인덱스 s_idx, 끝 인덱스 e_idx, 현재 위치 current
# 시작인덱스는 맨 앞이다(초기화가 필요함), 끝 인덱스는 현재 위치 하나 앞이다.
# 현재 위치는 1번째 인덱스 부터 시작된다.
N = int(input());
arr = list(map(int, input().split()));
arr.sort();
count = 0;

# current의 번호 마다 필요하다 즉, for(current < N)
# 그 안에서 while s_idx < e_idx인 동안
# arr[s_idx] + arr[e_idx] == arr[current]이면 current ++;
# arr[s_idx] + arr[e_idx] > arr[current]이면 e_idx--;
# arr[s_idx] + arr[e_idx] < arr[current]이면 s_idx++;
# ----
# 오류 1, 이거는 위치 지정이 아니라 전체를 다 탐색해야함
# 그러니까 current(현재위치)는 0부터 그리고 s, e_idx는 양 끝에서 시작하여 탐색을 시작해야 한다.


# 초기화 중복으로 인해 그냥 이 안에서 계속 초기화 해주면 됨
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