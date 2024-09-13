# N개의 재료
# 신맛 S , 쓴맛 B
# 신맛은 사용한 재료의 신맛의 곱이고, 쓴맛은 합이다.
# 재료는 적어도 하나
# 신맛과 쓴맛의 차이가 가장 작은 음식을 만들어라
# 재료 하나에 신맛, 쓴맛이 있는거임


def recur(idx, S, B, use):
    global answer
    if idx == N:  # 기저조건: 0번 인덱스부터 N까지 닿으면 종료
        if use >= 1:  # 재료를 하나도 사용하지 않았을 때 제외
            answer = min(answer, abs(S - B))
        return

    # 재료를 사용할 때
    recur(idx + 1, S * ingredient[idx][0], B + ingredient[idx][1], use + 1)

    # 재료를 사용하지 않을 때
    recur(idx + 1, S, B, use)


N = int(input())
ingredient = [list(map(int, input().split())) for _ in range(N)]

answer = 1e9

recur(0, 1, 0, 0)  # S는 곱이기 때문에 1
print(answer)
