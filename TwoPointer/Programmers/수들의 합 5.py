# https://www.acmicpc.net/problem/2018

'''
시작점과 끝점이 첫번째 원소의 인덱스를 가리키도록 한다.
현재 부분 합이 M과 같다면 카운트한다.
현재 부분 합이 M보다 작다면 end를 1 증가시킨다.
현재 부분 합이 M보다 크거나 같다면 start를 1 증가시킨다.
모든 경우를 확인할 때까지 2-4번 과정을 반복한다.
'''

from sys import stdin

sum = 0
count = 0
end = 1
n = int(stdin.readline())

# 1부터 n까지 증가
for start in range(1, n+1):
    # sum이 n보다 작고 end가 n보다 작거나 같을 때 sum에 더할 수 있기 때문에 그동안 반복
    while sum < n and end <= n:
        sum = sum + end
        end = end + 1

    # sum과 n이 같다면 count
    if sum == n:
        count = count + 1

    # 다르다면 start가 1증가되어야 하기 때문에 이전의 start 값은 필요가 없어짐
    # 따라서 현재의 start 값을 빼줌
    sum = sum - start

print(count)