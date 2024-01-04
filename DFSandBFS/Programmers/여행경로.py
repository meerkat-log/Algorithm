# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    # 정답 저장을 위한 배열(여러 가지의 경로가 나올 수 있음)
    answer = []
    # 사용한 티켓을 표시하기 위한 배열
    visited = [False] * len(tickets)

    # 재귀 방식을 사용한 bfs 함수
    # airport에는 출발지의 공항 이름
    # path에는 현재까지의 경로
    def dfs(airport, path):
        # path의 결과가 tickets + 1의 결과와 같을 때 해당 경로를 저장.
        # ticket을 모두 사용하면 경로는 tikets의 개수보다 1더 많기 때문.
        if len(path) == len(tickets) + 1:
            answer.append(path)

        # enumerate 함수는 index도 함께 알고 싶을 때 사용.
        # ticket을 다 사용하기 위한 반복문
        for index, ticket in enumerate(tickets):
            # 출발지 공항의 이름과 티켓의 출발지 이름이 같고 사용하지 않은 티켓일 경우일 때만
            if airport == ticket[0] and visited[index] == False:
                # 티켓을 사용했다는 표시
                visited[index] = True
                # 재귀를 통해 다시 도착지에서 시작하는 티켓을 찾을 수 있도록 bfs 함수 호출.
                # path + [ticket[1]]을 통해 현재까지의 경로도 함께 전달.
                dfs(ticket[1], path + [ticket[1]])
                # 다른 경로가 나올 수 있기 때문에 True로 표시했던 티켓을 False 변경.
                visited[index] = False

    # bfs 탐색 시작. 시작은 항상 ICN 공항이기 때문에 전달되는 값들은 ICN
    dfs(airport="ICN", path=["ICN"])

    # 여러개의 경로가 나왔을 경우 알파벳 순서가 앞서는 경로를 return해야 하기 때문에 정렬
    answer.sort()
    return answer[0]
