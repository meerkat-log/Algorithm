import heapq
from sys import stdin

cities = int(stdin.readline())
buses = int(stdin.readline())
route = [[] for _ in range(cities+1)]

for _ in range(buses):
    src, dst, cost = map(int, stdin.readline().split())
    route[src].append([dst, cost])

start, end = map(int, stdin.readline().split())

result = [float("inf")] * (cities+1)
heap = []
result[start] = 0

heapq.heappush(heap, [0, start])
while heap:
    cost, city = heapq.heappop(heap)

    if result[city] < cost:
        continue
    for now_city, fare in route[city]:
        now_cost = cost + fare
        if now_cost < result[now_city]:
            result[now_city] = now_cost
            heapq.heappush(heap, [now_cost, now_city])

print(result[end])
'''
def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])  # 최소힙은 배열의 첫 번째 값을 기준으로 배열을 정렬.
    INF = float('inf')
    weights = [INF] * (vertex + 1)  # DP에 활용할 memoization 테이블 생성
    weights[start] = 0  # 자기 자신으로 가는 사이클은 없으므로.

    print(weights)
    while heap:
        weight, node = heapq.heappop(heap)
        if weight > weights[node]:  # 비용 최적화 전부터 큰 비용일 경우 고려할 필요 없음.
            continue

        for n, w in graph[node]:  # 최소 비용을 가진 노드를 그리디하게 방문한 경우 연결된 간선 모두 확인
            W = weight + w
            if weights[n] > W:  # 여러 경로를 방문해 합쳐진 가중치 W가 더 비용이 적다면
                weights[n] = W  # 업데이트
                heapq.heappush(heap, (W, n))  # 최소 비용을 가진 노드와 합쳐진 가중치 추가

    return weights


vertex, edge, start = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]
for i in range(vertex + edge):
    src, dst, weight = map(int, input().split())
    graph[src].append([dst, weight])

weights = dijkstra(start)
print(weights)  # [inf, 0, 3, 5, 6, 8]
'''