n = int(input())  # 일
timeTable = [list(map(int, input().split())) for _ in range(n)]  # (상담 T , 금액 P)
dp = [0 for _ in range(n + 1)]  # dp: i 일 부터 n 일 까지 벌 수 있는 최대 금액.
# 조건: 만약 i일의 + T를 한 값이 n 보다 크면 선택하지 않고 다음으로 넘어간다.
# 조건: 만약 i일의 + T를 한 값이 < n 이면, i 일의 P를 더해간다.
# 첫 날부터 더해 나가는 것은 계속 sum을 해야함.
# 뒤에서부터 해나가야한다?
print(timeTable)
print(dp)
for i in range(n - 1, -1, -1):
    if i + timeTable[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + timeTable[i][0]] + timeTable[i][1], dp[i + 1])

print(dp)
print(max(dp))
