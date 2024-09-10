N, K = map(int, input().split())

array = list(map(int, input().split()))

prefix = [0 for _ in range(N + 1)]

# 해당 자리 까지의 누적합 생성
for i in range(N):
    prefix[i + 1] = prefix[i] + array[i]

answer = []
for i in range(K, N + 1):
    answer.append(prefix[i] - prefix[i - K])

print(max(answer))
