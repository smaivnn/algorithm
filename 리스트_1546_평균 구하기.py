# 과목 갯수 입력받기
n = int(input());

# 시험 성적을 입력 받는다, 리스트의 형식의 int형으로
score = list(map(int, input().split()));

# 최댓값을 선정한다.
maxScore = max(score);

# 값을 더한다.
sum = sum(score)

# 값을 출력한다.
print((sum / maxScore * 100) / n )