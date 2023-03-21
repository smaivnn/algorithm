# N개의 수를 정렬하고 앞에서부터 K번째 수를 출력하는 문제.
# 나중에 다른 정렬 알고리즘으로 풀어보기
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

print(f"{arr[k-1]} ")