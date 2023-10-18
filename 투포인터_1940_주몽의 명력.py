# 시간 초과
# import sys
# input = sys.stdin.readline;

# N = int(input())
# M = int(input())
# A = list(map(int, input().split()));
# start = 0;
# value = 1;
# count = 0;

# A.sort();

# while start < len(A)-1  :
#   if value == len(A) :
#     start = start + 1;
#     value = start + 1;
#   if A[start] + A[value] < M :
#     value += 1;
#   elif A[start] + A[value] == M :
#     count += 1;
#     value += 1;
#   else :
#     start = start + 1;
#     value = start + 1;

# print(count)

import sys
input = sys.stdin.readline;

# 변수들을 초기화 한다. 재료갯수 N, 번호 합 M, 재료들 배열 arr
# 정답 값 count, 시작인덱스 start_idx, 끝인덱스 end_idx
N = int(input());
M = int(input());
arr = list(map(int, input().split()));
count = 0; start_idx= 0; end_idx = N-1;

# 오름 차순으로 list를 변경한다.
arr.sort();

# 반복문, 언제까지? start_idx < end_idx인 동안 계속
# 만약 s_idx + e_idx == M 이면 -> s_idx++, e_idx--해주고 count를 올린다.
# 만약 s_idx + e_idx > M 이면 e_idx-- 해준다.
# s_idx + e_idx < M이면 s_idx++ 해준다.
while start_idx < end_idx :
    if arr[start_idx] + arr[end_idx] == M :
        start_idx += 1;
        end_idx -= 1;
        count += 1;
    elif arr[start_idx] + arr[end_idx] > M :
        end_idx -= 1;
    else:
        start_idx += 1;
print(count);