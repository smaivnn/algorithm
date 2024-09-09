def count_possible_answers(hints):
    possible_answers = 0

    for a in range(1, 10):
        for b in range(1, 10):
            if b == a:
                continue
            for c in range(1, 10):
                if c == a or c == b:
                    continue

                valid = True
                for hint in hints:
                    number, strike, ball = hint
                    strike_count = 0
                    ball_count = 0
                    digits = [int(digit) for digit in str(number)]

                    if a == digits[0]:
                        strike_count += 1
                    elif a in digits:
                        ball_count += 1
                    if b == digits[1]:
                        strike_count += 1
                    elif b in digits:
                        ball_count += 1
                    if c == digits[2]:
                        strike_count += 1
                    elif c in digits:
                        ball_count += 1

                    if ball != ball_count or strike != strike_count:
                        valid = False
                        break

                if valid:
                    possible_answers += 1

    return possible_answers


# 입력 처리
n = int(input())
hints = []
for _ in range(n):
    number, strike, ball = map(int, input().split())
    hints.append((number, strike, ball))

# 가능한 답의 총 개수 출력
print(count_possible_answers(hints))
