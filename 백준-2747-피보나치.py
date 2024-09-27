n = int(input())
print(n)

fibo = [0 for _ in range(n + 1)]
print(fibo)

# 점화식 : n = n-1 + n-2
fibo[0] = 0
fibo[1] = 1

for i in range(2, n + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

print(fibo)
print(fibo[n])
