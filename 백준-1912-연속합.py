# 연속된 수 중 가장 큰 합을 구하는 방법
n = int(input())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(n + 1)]

for i in range(n):
    prefix[i + 1] = max(prefix[i] + arr[i], arr[i])

print(max(prefix[1:]))
