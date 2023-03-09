# x y 사각형의 합을 구하는 문제
# x2, y2까지의 구간 합에서 
# 합배열을 구하는 공식 : s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j]
# 합배열 구간을 구하는 공식(문제) : s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1] 
# 
# 풀이 순서 :
# 필요한 입력을 받는다 > 합배열을 만든다 > 공식을 적용한다.

# 의사코드
import sys;
input = sys.stdin.readline;
# 입력받기
# N : 표의 크기, M : case 횟수
# arr = 표(채우는 수 입력받기)
N, M = map(int, input().split());
arr = list();
# print(f"{arr}")
for i in range(N) :    
  arr_row = list(map(int, input().split()));
  arr.append(arr_row);
# print(f"{arr}")

# 합배열 생성 
# sumArr = arr보다 1 1씩 더 큰 배열이며 0번째 행, 열은 arr의 0번째 행, 열과 동일
# sumArr[1,1] = arr[1,1]
# 이중for문으로 생성
sumArr = [[0 for j in range(N+1)] for i in range(N+1)];
for i in range(1, N+1) :
  for j in range(1, N+1) :
    sumArr[i][j] = sumArr[i-1][j] + sumArr[i][j-1] - sumArr[i-1][j-1] + arr[i-1][j-1]
# print(sumArr)


# 공식 적용
# for i in range(M) :
# 값 입력받기
# 입력받는 x1,x2,y1,y2를 s식에 적용한다.
for i in  range(M) :
  x1,y1,x2,y2 = map(int, input().split());
  print(f"{sumArr[x2][y2] - sumArr[x2][y1-1] - sumArr[x1-1][y2] + sumArr[x1-1][y1-1] }")

