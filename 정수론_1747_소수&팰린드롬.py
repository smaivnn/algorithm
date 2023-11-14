"""
n이 주어졌을때 n보다 큰 소수이면서 팰린드롬인 가장 작은 수를 찾는 문제.
팰린드롬 수 : 101, 324423과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수.

<< 아이디어 >>
n보다 큰 소수를 찾는것이므로 그냥 최대값까지 모든 소수를 다 구해버린 다음 그 중 팰린드롬수를 찾는다.

<< 슈도코드 >>
n을 입력받는다.
arr = 2~10000000까지의 배열을 만든다.

for i in range(2, 10000000)
  if arr[i] == 0이라면
    continue
  for j in range(i+i, 10000000, i)
    arr[j] = 0

for i in range(n+1, 10000000)
  if arr[i] != 0이라면
    if i가 팰린드롬수라면
      print(i)
      break
      
def isPalindrome(n):
  n = str(n)
  if n == n[::-1]:
    return True
  else:
    return False-
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = [i for i in range(10000001)]

for i in range(2, len(arr)):
    if arr[i] == 0:
        continue
    for j in range(i + i, len(arr), i):
        arr[j] = 0

for i in range(n, len(arr)):
    if i == 1:
        continue
    if arr[i] != 0:
        if str(i) == str(i)[::-1]:
            print(i)
            break
