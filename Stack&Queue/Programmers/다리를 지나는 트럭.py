# https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 시간을 구하기 위한 변수
    time = 0
    # 현재 다리에 올라가 있는 트럭을 표시하기 위한 큐
    on_bridge = deque([0]*bridge_length)
    # truck_weights를 리스트에서 deque로 변경
    truck_weights = deque(truck_weights)
    # 현재 다리에 올라가 있는 트럭의 무게
    bridge_weight = 0

    # truck_weights가 존재하는 동안 반복
    # 모든 트럭을 다리를 건너야 하기 때문
    while truck_weights:
        # 한 번 반복될 때마다 1초씩 증가
        time += 1

        # 한 번 반복될 때마다 다리에서 트럭이 이동해야 하므로 무조건 한 번은 빼야함.
        bridge_weight -= on_bridge.popleft()
        
        # 다리에 있는 트럭의 무게와 아직 올라가지 않은 트럭의 무게가 넘어갈 수 있는 weight와 작거나 같다면 트럭 추가
        if bridge_weight + truck_weights[0] <= weight:
            bridge_weight += truck_weights[0]
            on_bridge.append(truck_weights.popleft())
        # 트럭이 올라갈 수 없다면 0으로 설정
        else:
            on_bridge.append(0)

    # 마지막 트럭이 올라가면 반복이 종료되므로 바로 bridge_length만큼 시간 추가
    time += bridge_length

    return time


print(solution(2, 10, [7,4,5,6]))