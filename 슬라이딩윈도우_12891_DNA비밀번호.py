import sys
input = sys.stdin.readline;

# 변수 입력 받기
# S 문자열, P 부분 문자열, arr 부분 문자열list, ACGT 검증list
# 아이디어 : 검증List는 입력 받은 수 만큼으로 설정한다.
# 이후 윈도우 내에서 해당 검증 리스트의 것이 몇 개 있느냐 만큼 뺀다.
# 모든 리스트가 음수이면 검증된것.

S, P = map(int, input().split());
arr = list(input());
ACGTlist = list(map(int, input().split()));
start_idx, end_idx = 0, P-1;
count = 0;
A, C, G, T = ACGTlist[0], ACGTlist[1], ACGTlist[2], ACGTlist[3];

# for i in range(start_idx, end_idx + 1) :
while end_idx < S :
    # print(f"start : {start_idx}, end : {end_idx}")
    if (start_idx > end_idx) :
        if A < 1 and C < 1 and G < 1 and T < 1:
            count += 1;
            # print(f"A : {A}, C : {C}, G : {G}, T : {T}")
        A, C, G, T = ACGTlist[0], ACGTlist[1], ACGTlist[2], ACGTlist[3];
        end_idx += 1;
        start_idx = end_idx - ( P - 1);

    if arr[start_idx] == 'A':
        A -= 1;
    elif arr[start_idx] == 'C':
        C -= 1;
    elif arr[start_idx] == 'G':
        G -= 1;
    elif arr[start_idx] == 'T':
        T -= 1;
    start_idx += 1;


print(count);