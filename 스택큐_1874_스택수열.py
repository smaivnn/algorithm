import sys;
input = sys.stdin.readline;

n = int(input());
arr = [0] * n;
stack = [];

for i in range(n) :
    arr[i] = int(input());

for i in range(n) :
  if i + 1 <= arr[i]  :
    stack.append(i + 1);
    print(f"stack : {stack}");
  stack.pop();
  print(f"stack : {stack}");


  # arr값보다 스택 값이 작으면 다시 push한다.
  # 만약 스택의 젤 윗값이 같다면 pop한다.
  
  # 
