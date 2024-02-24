# https://school.programmers.co.kr/learn/courses/30/lessons/42584
import queue
from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    count = 0
    check = False

    while queue:
        price = queue.popleft()

        for idx, next_price in enumerate(queue):
            if price > next_price:
                answer.append(idx+1)
                check = True
                break
            else:
                count += 1
        if not check:
            answer.append(count)
        check = False
        count = 0

    return answer

print(solution([1,2,3,2,3]))