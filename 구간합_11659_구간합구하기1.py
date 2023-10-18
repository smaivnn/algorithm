# N개의 수에서 i to j까지 더하는 프로그램.
# N : 수의 개수, M : 합을 구해야 하는 횟수
# list : N개의 수
# M개의 Case, 구간 i j

# 풀이
# 리스트에 입력을 받는다.
# 받음과 동시에 합배열을 생성한다.
# 합 배열에서 뺴기(-)를 통해 진행한다.

import sys;
input = sys.stdin.readline;

N, M = map(int, input().split());
Nlist = list(map(int, input().split()));
sumList = [0];

for i in range(N) :
    print(i)
    sumList.append(sumList[i] + Nlist[i]);

for _ in range(M) :
    i, j = map(int, input().split());
    print(f"{sumList[j] - sumList[i-1]}")


