import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())

# 2, 3, 5, 7로 시작하는 부분만 시작하면 된다
# 소수인지 판별하는 함수가 필요하다
# DFS로 들어가는 부분은 짝수는 제외한 홀수만이다.
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def dfs(num):
    if len(str(num)) == n:
        print(num)
        return
    for i in range(1, 10, 2):  # 홀수 마다
        if isPrime(num * 10 + i):  # 그 수(합쳐진 수 )가 소수인지 판별
            dfs(num * 10 + i)


dfs(2)
dfs(3)
dfs(5)
dfs(7)