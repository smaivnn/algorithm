n = int(input())
tileTable = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if i == 1:
        tileTable[i] = 1
        continue
    if i == 2:
        tileTable[i] = 2
        continue
    tileTable[i] = tileTable[i - 1] + tileTable[i - 2]

print(tileTable[-1] % 10007)
