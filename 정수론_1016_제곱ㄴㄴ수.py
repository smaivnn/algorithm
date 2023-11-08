"""
어떤 수가 1보다 큰 제곱수로 나누어 떨어지지 않을 때 제곱ㄴㄴ수라고 하는데, min <= x <= max인 제곱ㄴㄴ수가 몇개인지 
예를들어 1~10사이에는
2의 제곱수 : 4, 8
3의 제곱수 : 9
을 제외한 나머지 1, 2, 3, 5, 6, 7, 10이다. 총 7개 이다.

< 아이디어 >
에라토스테네스의 체의 방식을 이용해서 배열 내의 제곱수들을 모두 제외한다.

메모리 줄이기 아이디어가 있는 문제

"""
"""
import sys
import math

input = sys.stdin.readline

min, max = map(int, input().split())
arr = [True for i in range(max + 1)]
check = []
count = 0

for i in range(2, int(math.sqrt(max)) + 1):
    j = i * i
    while j <= max:
        check.append(j)
        j = j * i


for i in range(min, max + 1):
    for j in range(len(check)):
        if i % check[j] == 0:
            arr[i] = False
            break


for i in range(min, max + 1):
    if arr[i] == True:
        count += 1
print(count)
"""
import sys
import math

input = sys.stdin.readline

min, max = map(int, input().split())
# arr = [True for i in range(max + 1)]
arr = [True] * (max - min + 1)
count = 0

for i in range(2, int(math.sqrt(max)) + 1):
    pow = i * i
    for j in range(min // pow, max // pow + 1):
        if j * pow >= min:
            # arr[j * pow] = False
            arr[j * pow - min] = False

# for i in range(min, max + 1):
for i in range(max - min + 1):
    if arr[i] == True:
        count += 1
print(count)
