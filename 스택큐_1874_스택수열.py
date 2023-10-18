import sys;
input = sys.stdin.readline;

N = int(input())
A = [0] * N 

for i in range(N) :
  A[i] = int(input());

stack = []
num = 1;
result = True;
answer = ""

for i in range(N) :
  su = A[i] # 현재 수열 값
  if su >= num : # 현재 수열 값 >= 오름차순 자연수
    while su >= num : # 값이 같아질 때 까지 append()수행
      stack.append(num)
      num += 1
      answer += "+\n"
    stack.pop() # 같이 같아질때까지 push를 한 후 pop을 통해 해당 값 출력
    answer += "-\n"
  else : # 현재 수열 값 < 오름차순 자연수
    n = stack.pop() # pop()을 통해 수열 원소를 꺼낸다.
    if n > su :
      print("NO")
      result = False;
      break;
    else : 
      answer += "-\n"
if result :
  print(answer)