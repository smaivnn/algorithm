# N과 M이 주어질 때 조건을 만족하는 길이가 M인 수열을 구해라
# 조건: 1부터 N까지 자연수 줄에서 중복 없이 M개를 고른 수열

# In: 4 2
# Out:
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3


def recur(number, output):
    if number == M:
        print(output)
        return

    for i in range(1, N + 1):
        if visited[i] == False:
            visited[i] = True
            recur(number + 1, output + str(i) + " ")
            visited[i] = False


N, M = map(int, input().split())

visited = [False for _ in range(N + 1)]
recur(0, "")

# -----------------------------------------------------
# 아래는 순열 사용하는 방법
# perms = permutations(range(1, N + 1), M)는 1부터 N까지의 숫자 중에서 M개를 뽑아 순서를 고려한 모든 순열을 생성합니다.
from itertools import permutations

N, M = map(int, input().split())

# 1부터 N까지의 숫자로 이루어진 리스트에서 M개의 숫자를 뽑은 순열 생성
perms = permutations(range(1, N + 1), M)
# perms: 
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 1)
# (2, 3)
# (2, 4)
# (3, 1)
# (3, 2)
# (3, 4)
# (4, 1)
# (4, 2)
# (4, 3)

# 각 순열을 출력
for perm in perms:
    print(" ".join(map(str, perm)))
