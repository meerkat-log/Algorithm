# https://school.programmers.co.kr/learn/courses/30/lessons/42898

# m : 열
# n : 행
def solution(m, n, puddles):
    # 입력된 값을 그래도 사용하기 위해 행렬에 각각 +1을 함
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    # 집의 위치를 1로 설정
    dp[1][1] = 1

    # 물 웅덩이 위치를 -1로 설정
    for x, y in puddles:
        dp[y][x] = -1

    # 집(1,1)부터 학교(n,m)까지 가야 하기 때문에 이중 반복문 사용
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 하나씩 이동하면서 물웅덩이가 있다면 경우의 수를 구할 때 영향을 주면 안되기 때문에 0으로 표시
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            # 현재 위치에서 나올 수 있는 경로의 가지수를 구한 후 1000000007로 나눈 나머지를 저장.
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007 + dp[i][j]

    return dp[n][m]


print(solution(4, 3, [[2, 2]]))