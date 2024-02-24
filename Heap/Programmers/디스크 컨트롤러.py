# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    answer = 0

    jobs = sorted(jobs, key=lambda x: x[1])
    print(jobs)

    heapq.heapify(jobs)

    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))