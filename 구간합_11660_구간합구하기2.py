import sys;
input = sys.stdin.readline;

# << 입력
# 표의 크기 N과, 합을 구해야하는 횟수 M을 입력 받는다.
# N개의 줄 만큼 배열의 인덱스들을 입력받는다.
# M번 만큼 크기를 구해야 하는 좌표를 입력받는다.

# N(리스트 크기), M(질의 수)
N, M = map(int, input().split());

# A(원본 배열), S(합 배열)
A = [[0] * (N + 1)]
S = [[0] * (N + 1) for _ in range(N + 1)]

# for : 원본 배열 저장
for i in range(N) :
  A_row = [0] + [int(x) for x in input().split()] # === A_row.insert(0, 0)
  A.append(A_row)



# for : 합 배열 저장
for i in range(1, N + 1) :
  for j in range(1, N + 1) :
    S[i][j] = S[i][j-1] + S[i-1][j] - S[i-1][j-1] + A[i][j];

# for : m번만큼 좌표 출력
for _ in range(M) :
  x1, y1, x2, y2 = map(int, input().split());
  answer = S[x2][y2] - S[x2][y1-1] - S[x1-1][y2] + S[x1-1][y1-1]
  print(answer)