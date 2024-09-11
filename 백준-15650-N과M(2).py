def recur(start, number, output):
    if number == M:
        print(output)
        return

    for i in range(start, N + 1):
        recur(i + 1, number + 1, output + str(i) + " ")


N, M = map(int, input().split())
visited = [False for _ in range(N + 1)]
recur(1, 0, "")


# -----------------------------------------------------
# 아래는 조합 사용하는 방법
# combs = combinations(range(1, N + 1), M)는 1부터 N까지의 숫자 중에서 M개를 뽑아 순서 상관없이 모든 조합을 생성합니다.
from itertools import combinations

N, M = map(int, input().split())

# 1부터 N까지의 숫자로 이루어진 리스트에서 M개의 숫자를 뽑은 조합 생성
combs = combinations(range(1, N + 1), M)
# combs:
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)
# (3, 4)


# 각 조합을 출력
for comb in combs:
    print(" ".join(map(str, comb)))
