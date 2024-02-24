# https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq

def solution(operations):
    # 최소 힙과 최대 힙을 위한 리스트
    min_heap = []
    max_heap = []

    # 명령어를 하나씩 가져와서 추가하고 삭제하는 과정 진행.
    for operation in operations:
        operation = operation.split(" ")

        # I일 때는 값 추가
        if operation[0] == "I":
            # 최소 힙에는 그대로 추가하고 최대 힙에는 -를 붙여 음수로 저장해야 나중에 최대로 사용 가능
            heapq.heappush(min_heap, int(operation[1]))
            heapq.heappush(max_heap, -int(operation[1]))

        # D일 때는 삭제를 진행
        elif operation[0] == "D":
            # 힙에 값이 없을 때는 패스
            if len(min_heap) == 0 or len(max_heap) == 0:
                continue
            # 명령어가 1이면 최댓값 삭제
            elif operation[1] == "1":
                min_value = -(heapq.heappop(max_heap))
                min_heap.remove(min_value)
            # 명령어가 -1이면 최솟값 삭제
            elif operation[1] == "-1":
                max_value = -(heapq.heappop(min_heap))
                max_heap.remove(max_value)

    # 힙이 비어있으면 [0, 0]을 반환하고 아니면 [최댓값, 최솟값]으로 반환
    return [-(heapq.heappop(max_heap)), heapq.heappop(min_heap)] if len(min_heap) > 0 else [0, 0]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
