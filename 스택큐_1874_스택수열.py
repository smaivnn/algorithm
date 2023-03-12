# 1부터 n까지의 수를 스택에 저장하고, 이를 출력하면서 수열을 만들어진다.
# 이 과정에 push하는 순서는 무조건 오름차순이어야 한다.
# 어느 수열이 주어졌을때, 위의 과정을 거치며 이 수열을 만들 수 있는가를 확인하는데 
# 만들 수 있다면 push와 pop의 순서가 어떻게 되느냐 ?
# 즉, 임의로 주어지는 수열을, 1~N까지의 순서로 저장되는 스택을 통해 만들어라. 그 과정에서 push pop과정을 보여라.

# 풀이 생각
# 수열의 현재 값 > 스택 값 ? push : pop
# 그런데 pop한 값이 수열의 현재 값과 다르다면 No를 출력한다.


# 의사코드
# ---------------
# 다시 생각해야 할 것 : 다음에 들어올 stack값을 for i 변수로설정하면 안됨.
# 따로 변수를 만들어서 통제해주어야 함.
import sys;
input = sys.stdin.readline;
# n 갯수입력
# n 만큼 수열을 한 줄당 list에 받는다.
# stack 스택, arrValue 수열 현재 선택 값, stackValue :스택에 넣는 값
n = int(input());
arr = [0] * (n + 1);
for i in range(1, n + 1) :
    arr[i] = int(input());
stack = list();
arrValue, stackValue = 1, 1 ;
result = "";


# for i in n만큼 (스택 값) XXXX틀림XXXXX
# 스택에 i를 push.
# 만약 i > 스택값이면 pop한다.
# 그런데 만약 pop한 값이 수열의 현재 값다 다르면 NO를 출력해야한다.
while arrValue < len(arr) :
  if stackValue <= arr[arrValue] :
    stack.append(stackValue);
    result += "+\n"
    stackValue += 1;
    # print(f"{stack}");
  else :
    popValue = stack.pop();
    result += "-\n"
    if popValue == arr[arrValue] :
      # print(f"{popValue}");
      arrValue += 1;
    else :
      result = "NO"
      break;
      

print(f"{result}")