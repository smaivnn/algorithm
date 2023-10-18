"""
# 문제 풀이 실패 (내 풀이가 맞지 않음)

# 내 풀이--------------------------------------------------------------
# 입력받은 배열을 윈도우 단위로 확인한다.
# 필요한거 : 원본 입력 배열, 숫자 저장 배열, 윈도우 배열, 윈도우 크기
# 1. for문에서 윈도우 크기만큼의 배열을 넣는다.
# 2. 이 배열이 갖고있는 알파벳만큼 숫자를 더한다.
# 3. 다음 칸으로 이동할 때, 윈도우의 맨 앞 인덱스([0])번째를 뺀다. 이 때 if문을 통해 알파벳 확인 후 해당하는 숫자저장배열에서 뺴기
# 4. 이동 후 윈도우의 새로추가된 맨 뒤인덱스([3])번째를 확인, if문을 통해 숫자 배열 올리기.
# 5. 만약 ACGT조건과 비교 후 값 초과가 되면 count 올리기.

# 의사코드
# S DNA문자열길이, P 부분 문자열 길이, DNAList 원본 입력 배열, DNACount 숫자 체크 원본 배열, windowList : 윈도우 배열, windownDNACount : 윈도우 숫자 체크배열, count 답
# 원본 입력 배열에서 부분 문자열 길이만큼 window배열에 저장한다.
# 숫자 저장배열에 해당하는 갯수만큼 저장한다.
# 배열의 맨 앞을 확인한다. 숫자배열에서 뺸다.
# 윈도우를 옮긴다. 배열의 맨 뒤를 확인한다. 숫자 배열에 더한다.
# 이를 마지막까지 반복한다.
# ---------------------------------------------------------------------

checkList = [0] * 4; # DNA비밀번호 체크배열
myList = [0] * 4; # 윈도우의 현재 상태
checkSecret = 0; # 몇 개의 문자와 관련된 개수를 충족했는지 판단한다.

def myadd(c) : 
    global checkList, myList, checkSecret;
    if c == 'A' : # 만약 입력받은 글자가 A라면 
        myList[0] += 1 # 현재 상태에 + 1
        if myList[0] == checkList[0] : # 내 현재 값이 윈도우 체크배열의 값과 같다면
            checkSecret += 1; # 하나올린다, 4가 되면 모두 충족이라는 뜻
    
    elif c == 'C' :
        myList[1] += 1;
        if myList[1] == checkList[1] :
            checkSecret += 1

    elif c == 'G' :
        myList[2] += 1;
        if myList[2] == checkList[2] :
            checkSecret += 1

    elif c == 'T' :
        myList[3] += 1;
        if myList[3] == checkList[3] :
            checkSecret += 1

def myremove(c) :
    global checkList, myList, checkSecret;
    if c == 'A' : # 입력받은 문자가 A라면
        if myList[0] == checkList[0] : # 
            checkSecret -= 1; # 
        myList[0] -= 1

    elif c == 'C' :
        if myList[1] == checkList[1] :
            checkSecret -= 1
        myList[1] -= 1

    elif c == 'G' :
        if myList[2] == checkList[2] :
            checkSecret -= 1
        myList[2] -= 1

    elif c == 'T' :
        if myList[3] == checkList[3] :
            checkSecret -= 1
        myList[3] -= 1



S, P = map(int, input().split()); # 문자열길이, 부분문자열 길이
Result = 0;
A = list(input()); # DNA문자열
checkList = list(map(int, input().split())); # DNA비밀번호 체크배열

# 몇개가 현재 완료되었나 (0인가? => 할 필요 없음)
for i in range(4) :
    if checkList[i] == 0 :
        checkSecret += 1

# 처음 부분배열에 대해서 검증함.
for i in range(P) :
    myadd(A[i])
    if checkSecret == 4 :
        Result += 1;

# 
for i in range(P, S) :
    j = i - P
    myadd(A[i]) # 부분문자열번째 처리
    myremove(A[j]) # 0번째 처리
    if checkSecret == 4 :
        Result += 1

print(Result)
"""
import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dnaList = list(input().strip())
dnaDic = {};
acgtList = list(map(int, input().split()));
acgtDic = {"A": 0, "C": 0, "G" : 0, "T": 0};
start, end = 0, p;
count = 0;

for i in range(p) :
    if dnaList[i] in dnaDic :
        dnaDic[dnaList[i]] += 1;
    else :
        dnaDic[dnaList[i]] = 1;


acgtDic["A"] = int(acgtList[0])
acgtDic["C"] = int(acgtList[1])
acgtDic["G"] = int(acgtList[2])
acgtDic["T"] = int(acgtList[3])
    

def checkDic(array, agctArray) :
    nucleotides = ["A", "C", "G", "T"]
    for key in nucleotides:
        if key not in array :
            array[key] = 0

    if array["A"] >= agctArray["A"] and array["C"] >= agctArray["C"] and array["G"] >= agctArray["G"] and array["T"] >= agctArray["T"]:
        return True
    return False


while end <= s :
    if checkDic(dnaDic, acgtDic) == True:
        count += 1
        if end == s :
            break;
        dnaDic[dnaList[start]] -= 1;
        dnaDic[dnaList[end]] += 1; 
        start += 1
        end += 1
    else :
        if end == s :
            break;
        dnaDic[dnaList[start]] -= 1;
        dnaDic[dnaList[end]] += 1; 
        start += 1
        end += 1

print(count)