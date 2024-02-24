# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    # 작업들이 걸린 시간을 저장하기 위한 변수
    answer = 0
    # 작업을 시작할 수 있는 시간과 현재 시간을 저장하기 위한 변수
    # start 변수보다 작업이 요청되는 시점이 크고 현재 시간보다 작거나 같을 때 힙에 추가 가능
    start, time = -1, 0
    # 완료한 작업의 개수를 저장하기 위한 변수
    count = 0
    # heap 리스트
    heap = []

    # jobs의 길이만큼 작업을 완료하면 종료
    while count < len(jobs):
        # jobs의 값을 하나씩 가져와서 작업이 요청되는 시점이 작업이 시작될 수 있는 시간보다 크면서 현재 시간과 작거나 같을 때
        # 힙에 작업의 소요 시간이 적은 것부터 힙에 추가.
        # 힙에 추가된 후에는 최소값으로 소요 시간이 적은 것부터 정렬됨.
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(heap, [job[1], job[0]])

        # 힙에 데이터가 존재할 때
        if heap:
            # 현재 힙에 작업의 소요 시간이 가장 같은 리스트를 꺼내온다.
            job = heapq.heappop(heap)
            # 작업이 실행되었기 때문에 start에는 현재 시간을 저장한다.
            # 작업이 존재하였기 때문에 중복되지 않고 다음 작업을 추가하기 위해서는
            # 작업이 요청되는 시점이 현재 시간이 time보다 작거나 같은 값이기 때문에
            # start에 현재 시간의 값인 time을 저장하여 다음 작업을 추가할 땐 start 보다 큰지 비교를 하여 중복을 방지한다.
            start = time
            # time은 작업의 소요 시간만큼 증가되어 저장된다.
            # 그 작업만큼의 시간이 흐른 뒤에 다른 작업을 할 수 있기 때문이다.
            time += job[0]

            # answer에는 작업의 총 시간이 저장되어야 하기 때문에
            # 현재 시간에서 작업이 요청되는 시점만큼의 시간을 빼서 추가한다.
            answer += time - job[1]
            # 하나의 작업이 완료되었기에 count가 하나 증가한다.
            count += 1
        else:
            # 실행할 수 있는 작업이 없을 경우 time이 1씩 증가하면서 작업이 요청되는 시점에 맞는 조건을 찾을 수 있도록 한다.
            time += 1


    # 평균 시간을 반환해야 하기 때문에 총 시간을 작업을 개수로 나누어 준다.
    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6], [0,5], [0,2], [0,1]]))