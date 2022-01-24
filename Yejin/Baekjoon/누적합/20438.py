import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep = set(map(int, input().split())) # k명
attend = set(map(int, input().split())) # q명
checked = [False for _ in range(n + 3)]

# 출석 체크
for a in (attend - sleep): # 여기서 (attend-sleep) 안해주면 에러 발생
  for i in range(a, n + 3, a): # 배수
    if i not in sleep:
      checked[i] = True

# 누적합: 출석하지 않은 학생 수 (졸고 있는 학생 + 출석 코드 받지 못한 학생)
students = [0 for _ in range(n + 3)]
for s in range(3, n + 3):
  if not checked[s]: # 출석 X
    students[s] = students[s - 1] + 1
  else:
    students[s] = students[s - 1]

# 구간합(부분합): 구간에 대해 출석하지 않은 학생 수
for _ in range(m):
  s, e = map(int, input().split())
  print(students[e] - students[s - 1])
