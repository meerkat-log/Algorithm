# https://www.acmicpc.net/problem/3273

from sys import stdin

# 수열의 크기 n
n = int(stdin.readline())
# 수열의 값을 입력받아 정렬된 리스트로 저장
lst = sorted(list(map(int, stdin.readline().split())))
# n + m 의 값으로 맞춰야 할 값.
# n < m
x = int(stdin.readline())

print(lst)

count, sum = 0, 0
i, j = 0, n-1

# n < m의 조건을 만족하기 위해 반복문의 조건도 i < j로 설정.
while i < j:
    sum = lst[i] + lst[j]

    # sum이 값이 x와 같다면 count
    if sum == x:
        count = count + 1
        i = i + 1
    # sum의 값이 작다면 i를 1 증가하여 더 큰 값을 만듦.
    # lst는 정렬되어 있기 때문에 왼쪽에서 하나씩 증가하면 값은 더 커짐.
    elif sum < x:
        i = i + 1
    # sum의 결과가 크다면 j의 값을 감소하여 최대값을 낮춰 sum의 결과를 감소시킴.
    else:
        j = j - 1

print(count)