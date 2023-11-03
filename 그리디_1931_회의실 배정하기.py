"""
회의실 배정 문제, 회의실에 가장 많은 회의를 배정하는 문제

<< 아이디어 >>
회의를 가장 많이 배정하려면 다음과 같은 조건이 필요하다.
1. 회의의 종료 시간이 빨라야한다.
  - 회의 종료 시간이 빠르다는 것은 시작 시간이 언제이든 일찍 끝난다는 뜻이다.
2. 회의 자체가 짧아야 한다.
  - 회의가 짧다는 것은 1번에 이어져 시작부터 종료 시간이 짧다는 거다.

  << 의사코드 >>
  n = 회의의 수
  회의 정보를 입력받는다.

  가장 종료 시간이 빠른 회의를 찾는다.
  그 회의를 배정한다.
  반복
    그 회의의 종료 시간 이후에 시작하는 회의들을 찾는다.
    그 회의들 중 가장 종료 시간이 빠른 회의를 찾는다.
    그 회의를 배정한다.
"""

import sys

input = sys.stdin.readline

n = int(input())
answer = 0
meetings = []
for _ in range(n):
    meetings.append(list(map(int, input().split())))

# 회의 종료 시간이 빠른 순으로 정렬, 종료 시간이 같으면 시작 시간이 빠른 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 가장 종료 시간이 빠른 회의를 찾는다.
pre_meeting = meetings[0]
answer += 1

# 그 회의의 종료 시간 이후에 시작하는 회의들을 찾는다.
for i in range(1, n):
    if pre_meeting[1] <= meetings[i][0]:
        answer += 1
        pre_meeting = meetings[i]

print(answer)
