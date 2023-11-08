"""
n개의 재료에 대해서 칵테일을 만드는데 필요한 재료의 질량을 구하는 문제

입력은 재료n과 n-1개의 칵테일의 조합이 줄만큼 주어진다.
이때 a,b,p,q형태로 주어지는데, a와 b는 칵테일을 만들기 위해 필요한 재료(인덱스)의 번호이고, p와 q는 그 재료의 질량이다.

예를들어 4 0 1 1 이라면 4번 재료 1 : 1 0번 재료 라는 뜻이다.

<< 아이디어 >>
4번과 각 인덱스에 관한 비율이 주어지기 때문에 각각의 비율에 대해서 최소공배수를 구한다. 최소공배수를 구하는 이유는 비율에 적용되는 정수 최소값을 구하기 위해서. 

<< 풀이 >>
일단 노드에 값을 넣으면서 
최소공배수를 뽑는다. 

<< 의사코드 >>


"""
import sys

input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n)]
visited = [False] * n
d = [0] * n
lcm = 1


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def dfs(x):
    visited[x] = True
    for i in arr[x]:
        next = i[0]
        if not visited[next]:
            d[next] = d[x] * i[2] // i[1]
            dfs(next)


# 인접 리스트에 값을 넣으며 최소공배수를 구한다.
for i in range(n - 1):
    a, b, p, q = map(int, input().split())
    arr[a].append((b, p, q))
    arr[b].append((a, q, p))
    lcm = lcm * (p * q // gcd(p, q))  # 최소 공배수. 최소 공배수는 두 값의 곱을 최대공약수로 나눈 값이다.

d[0] = lcm
print("d", d)
dfs(0)
print("d", d)
mgcd = d[0]

for i in range(1, n):
    mgcd = gcd(mgcd, d[i])
print(mgcd)

for i in range(n):
    print(int(d[i] // mgcd), end=" ")
