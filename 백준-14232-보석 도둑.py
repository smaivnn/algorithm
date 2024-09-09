# 소인수 분해 문제


def find_factors(k):
    factors = []
    # 2부터 시작해서 나눌 수 있는 소수를 찾는다. 즉 약수를 찾음.
    for i in range(2, int(k**0.5) + 1):
        # i로 나눌 수 있을 때마다 나눈다.
        while k % i == 0:
            factors.append(i)  # 일단 나누어 떨어진 그 값을 넣음
            k //= i
    # 남아있는 k가 소수일 경우 그것도 추가해야 한다.
    if k > 1:
        factors.append(k)
    return factors


# 입력 받기
k = int(input())

# 소인수 분해하여 결과를 출력
factors = find_factors(k)
print(len(factors))  # 보석의 개수 출력
print(" ".join(map(str, factors)))  # 보석의 무게들 출력
