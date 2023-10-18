import sys;
input = sys.stdin.readline;

# N(입력 수), M(질의 값)
N, M = map(int, input().split())
# A(원본 배열), S(합 배열)
A = list(map(int, input().split()))
S = [0] * N
C = [0] * M
S[0] = A[0]

count = 0;

# for -> 합배열 생성
for i in range(1, N) :
  S[i] = S[i-1] + A[i]

# for 합배열 % M
for i in range(N) :
  S[i] = S[i] % M
  C[S[i] % M] += 1
  if(S[i] == 0) :
    count = count + 1;

# 값이 같은 것을 찾는다. (조합)
# for 입력수 까지 그 값이 몇개인지 찾는다.
for i in range(M) :
  if C[i] > 1 : 
    count = count + (C[i] * (C[i] - 1)) // 2

print(count)