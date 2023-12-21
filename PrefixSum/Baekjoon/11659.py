# 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659

from sys import stdin

# N: 수의 개수, M: 합을 구해야 하는 횟수
n, m = map(int, stdin.readline().split())
num_list = list(map(int, stdin.readline().split()))

# result : 누적합을 저장하는 배열
result = [0]

# 누적합 구하는 반복문
for i in range(len(num_list)):
    result.append(result[i] + num_list[i])

# 결과 구하는 반복문
for i in range(m):
    start, end = map(int, input().split())
    print(result[end] - result[start-1])