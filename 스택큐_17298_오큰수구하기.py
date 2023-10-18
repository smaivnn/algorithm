N = int(input())
arr = list(map(int, input().split()))
stack = [];
answer = [0] * N

for i in range(N) :
    # 스택이 비어있지 않고 and 
    # 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
    while stack and arr[stack[-1]] < arr[i] :
        answer[stack.pop()] = arr[i] # 정답 리스트에 오큰수를 현재 수여롤 저장하기
    stack.append(i)
while stack : # 반복문을 다 돌고 나왔는데 스택이 비어있지 않다면 빌 때까지
    answer[stack.pop()] = -1 # 스텍에 쌓인 index에 -1을 넣기

result = ""

for i in range(N) :
    result += str(answer[i])+" "

print(result)