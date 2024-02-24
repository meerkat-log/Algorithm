# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    # n : 행
    # m : 열
    n = len(maps)
    m = len(maps[0])

    # (1, 1)을 그대로 사용하기 위한 확장 리스트 생성
    ext_maps = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            ext_maps[i+1][j+1] = maps[i][j]

    # 방문한 곳을 기록하기 위한 visited 리스트 생성
    # 시작은 항상 (1, 1)이기 때문에 True로 설정
    maps_visited = [[False for j in range(m+1)] for i in range(n+1)]
    maps_visited[1][1] = True

    def bfs(x, y):
        queue = deque()
        queue.append([x, y])

        while queue:
            x, y = queue.popleft()

            # 동
            if (x <= n and y < m) and (ext_maps[x][y+1] == 1 and maps_visited[x][y+1] == False):
                queue.append([x, y+1])
                maps_visited[x][y+1] = True
                ext_maps[x][y+1] = ext_maps[x][y] + 1

            # 서
            if (x <= n and y > 1) and (ext_maps[x][y-1] == 1 and maps_visited[x][y-1] == False):
                queue.append([x, y-1])
                maps_visited[x][y-1] = True
                ext_maps[x][y-1] = ext_maps[x][y] + 1

            # 남
            if (x < n and y <= m) and (ext_maps[x+1][y] == 1 and maps_visited[x+1][y] == False):
                queue.append([x+1, y])
                maps_visited[x+1][y] = True
                ext_maps[x+1][y] = ext_maps[x][y] + 1

            # 북
            if (x > 1 and y <= m) and (ext_maps[x-1][y] == 1 and maps_visited[x-1][y] == False):
                queue.append([x-1, y])
                maps_visited[x-1][y] = True
                ext_maps[x-1][y] = ext_maps[x][y] + 1

    bfs(1,1)
    return -1 if ext_maps[n][m] == 1 else ext_maps[n][m]

print(solution([
[1, 0, 1, 1, 1],
[1, 0, 1, 0, 1],
[1, 0, 1, 1, 1],
[1, 1, 1, 0, 0],
[0, 0, 0, 1, 1],
]))