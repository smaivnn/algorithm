# 선택된 값의 오른쪽에서 더 큰값이 있는지 탐색하고, 
# 그 중 가장 왼쪽(작은 아님)수를 출력하는 것.

# -----------------실패-----------------

n = int(input()); # 갯수 n
ans = [0] * n; # 정답 배열
A = list(map (int, input().split())); # 입력 배열
myStack = []; 

for i in range(n) :
    while myStack and A[myStack[-1]] < A[i] :
        ans[myStack.pop()] = A[i];
    myStack.append(i)
while myStack :
    ans[myStack.pop()]= -1

result = ""

for i in range(n) :
    result += str(ans[i]) + " "

print(result)
