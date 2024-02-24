# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    # 반복된 횟수를 구하기 위한 변수
    count = 0
    # scoville을 heapq로 사용하기 위한 처리.
    heapq.heapify(scoville)

    # heapq를 사용하면 0번 인덱스는 항상 최소값이다.
    # 따라서 0번 인덱스가 K 보다 작으면 반복한다.
    while scoville[0] < K:
        # 스코빌 리스트의 값이 1이면 더이상 스코빌을 증가시킬 수 없어 -1을 반환한다.
        if len(scoville) == 1:
            return -1

        # heapq에 새로 만들어낸 스코빌 값을 추가
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        count += 1

    return count

print(solution([1, 2, 3, 9, 10, 12], 7))

'''
import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)

    # min을 사용하면 리스트의 모든 값을 비교하기 때문에 효율성에서 통과할 수 없다.
    # 왜냐하면 하나하나 다 비교하여 최소갑을 찾기 때문.
    # 하지만 heapq를 사용하면 최소값은 0번 인덱스에 있기 때문에
    # min()을  사용할 필요가 없다.
    while min(scoville) < K:
        if len(scoville) == 1:
            return -1

        count += 1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))

    return count
'''