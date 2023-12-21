# https://school.programmers.co.kr/learn/courses/30/lessons/43162

# Queue를 사용하기 위한 라이브러리 호출
from collections import deque

def solution(n, computers):
    # 네트워크망의 개수를 위한 변수
    answer = 0
    # 방문한 곳을 확인하기 위한 리스트
    visited = [False] * n
    
    # BFS 방식으로 사용한  함수
    def bfs(index):
        # Queue 생성 후 현재의 컴퓨터 번호를 받아서 Queue에 저장
        queue = deque()
        queue.append(index)

        # Queue에 대기열이 존재하는 동안 반복
        while queue:
            # 큐에서 하나를 빼서 now 변수에 저장 후 방문 기록
            now = queue.popleft()
            visited[now] = True

            # 컴퓨터의 대수만큼 computers에 리스트가 존재하기 때문에 n번만큼 반복
            for i in range(n):
                # computers 2차원 리스트에서 현재 컴퓨터가 연결된 컴퓨터 중에서 방문하지 않은 컴퓨터를 Queue에 저장.
                if computers[now][i] == 1 and visited[i] == False:
                    queue.append(i)

    # 컴퓨터 대수만큼 반복
    for index in range(n):
        # 방문하지 않은 컴퓨터 번호에서 BFS 실행
        if visited[index] == False:
            bfs(index=index)
            answer = answer + 1

    return answer

print("정답: ", solution(n=3, computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
