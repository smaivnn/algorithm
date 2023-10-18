import sys
input = sys.stdin.readline;

# N(질의 자연수)
N = int(input())
# StartIdx(시작점), EndIdx(끝점)
startIdx = 1 ;
endIdx = 1;
# sum(합), count(답)
sum = 1;
count = 0;

while endIdx <= N and startIdx <= N:
  if sum < N :
    endIdx += 1;
    sum += endIdx;
  elif sum > N :
    sum -= startIdx;
    startIdx +=1;
  elif sum == N :
    count += 1;
    endIdx += 1;
    sum += endIdx;

print(count)