# 구간 합 구하기 5
# https://www.acmicpc.net/problem/11660
"""
n, m = map(int, input().split())

arr = [[0 for j in range(n+1)] for i in range(n+1)]
for i in range(1, n+1):
    num_list = list(map(int, input().split()))
    for j in range(1, n+1):
        arr[i][j] = num_list[j-1]

result = [[0 for j in range(n+1)] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        result[i][j] = result[i][j-1] + arr[i][j]

answer = [0] * m
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2+1):
        answer[i] = answer[i] + (result[j][y2] - result[j][y1-1])

for i in answer:
    print(i)

# 구간 합 구하기 5
# https://www.acmicpc.net/problem/11660

n, m = map(int, input().split())

result = [[0 for j in range(n+1)] for i in range(n+1)]
for i in range(1, n+1):
    num_list = list(map(int, input().split()))
    for j in range(1, n+1):
        result[i][j] = result[i][j - 1] + num_list[j-1]

answer = [0] * m
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2+1):
        answer[i] = answer[i] + (result[j][y2] - result[j][y1-1])

for i in answer:
    print(i)
"""
# 구간 합 구하기 5
# https://www.acmicpc.net/problem/11660
from sys import stdin

# N: 표의 크기, M: 합을 구해야 하는 횟수
n, m = map(int, stdin.readline().split())

# result: 2차원 배열의 누적합을 저장
result = [[0]*(n+1) for i in range(n+1)]
for i in range(1, n+1):
    num_list = list(map(int, stdin.readline().split()))
    for j in range(1, n+1):
        result[i][j] = result[i-1][j] + result[i][j-1] - result[i-1][j-1] + num_list[j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(result[x2][y2] - result[x1-1][y2] - result[x2][y1-1] + result[x1-1][y1-1])