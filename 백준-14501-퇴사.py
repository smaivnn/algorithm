# N 날짜
# (T 기간, P 금액)
# 선택하면 기간(T)일만큼 선택 불가능함


# idx: N번째 인덱스, price: P
def recur(idx, P):
    global answer
    if idx == N:
        answer = max(answer, P)
        return
    if idx > N:
        return

    # 날을 선택했을 경우
    recur(idx + counsel[idx][0], P + counsel[idx][1])

    # 선택하지 않았을 경우
    recur(idx + 1, P)


N = int(input())
counsel = [list(map(int, input().split())) for _ in range(N)]
answer = 0
recur(0, 0)

print(answer)
