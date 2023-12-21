# https://www.acmicpc.net/problem/1260

# 입력을 받기 위한 라이브러리 추가
from sys import stdin
# Queue를 사용하기 위한 라이브러리 추가
from collections import deque

# n : 정점의 개수
# m : 간선의 개수
# v : 탐색을 시작할 정점의 번호
n, m, v = map(int, stdin.readline().split())

# 2차원 배열로 연결 되어 있는 정점들을 표시할 배열 생성
# 정점의 개수보다 1개 더 큰 배열로 만들어 들어오는 입력을 그대로 사용.
# 배열에서는 0이 작은 값이지만 입력에서는 1이 작은 값이기 때문.
array = [[0 for j in range(n+1)] for i in range(n+1)]
for i in range(m):
    x, y = map(int, stdin.readline().split())
    array[x][y] = 1
    array[y][x] = 1

# dfs의 결과 값을 저장하기 위한 배열 생성
dfs_answer = []
# 방문한 정점을 알기 위한 배열 생성
dfs_visited = [[False for j in range(n+1)] for i in range(n+1)]

# dfs 함수에 현재 정점을 변수 v에 전달
def dfs(v):
    # 1부터 마지막 번호까지 반복
    for i in range(1, len(array)):
        # 현재 정점에서 다른 정점으로 연결된 것이 있고 방문한 기록이 없을 때 True
        if array[v][i] == 1 and dfs_visited[v][i] == False and dfs_visited[0][i] == False:
            # 따라 들어간 정점을 정답 배열에 추가
            dfs_answer.append(i)
            # 방문했다는 표시로 변경
            # dfs_visited[0]에는 연결된 정점들에서 이미 방문했던 곳이면 방문하지 않아야 하기 때문에 표시하는 값.
            dfs_visited[v][i] = True
            dfs_visited[0][i] = True
            # 따라 들어갈 정점으로 재귀함수 시작
            dfs(i)

# dfs를 처음 시작할 때 v의 값을 방문했다고 표시 후 정답 배열에 추가.
dfs_visited[0][v] = True
dfs_answer.append(v)
dfs(v)
print(*dfs_answer)

# bfs의 결과 값을 저장하기 위한 배열 생성
bfs_answer = []
# 방문한 정점을 알기 위한 배열 생성
bfs_visited = [[False for j in range(n+1)] for i in range(n+1)]

def bfs(v):
    # bfs에서는 queue를 사용하기 때문에 Queue 생성
    queue = deque()
    # queue에 시작 값 추가
    queue.append(v)

    # queue에 값이 존재하는 동안 반복
    while queue:
        # queue에서 맨 앞의 값을 꺼내 변수 now에 저장.
        now = queue.popleft()
        # now에 저장된 정점을 방문했다는 기록을 남김.
        bfs_visited[0][now] = True
        # for문이 작동하는 동안 방문했던 정점이 또 추가되는 문제가 있어 필터링
        if now not in bfs_answer:
            bfs_answer.append(now)

        # 작은 값인 1부터 끝 값까지 반복
        for i in range(1, len(array)):
            # now와 연결된 정점을 작은 수부터 queue에 추가하기 위한 조건
            if array[now][i] == 1 and bfs_visited[now][i] == False and bfs_visited[0][i] == False:
                # 조건 만족시 queue에 추가.
                queue.append(i)
                # 정점에 방문했다는 표시로 변경.
                bfs_visited[now][i] = True
    print(*bfs_answer)
bfs(v)
