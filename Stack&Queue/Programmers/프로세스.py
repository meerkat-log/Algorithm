# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    # 순서 번호 지정을 위한 변수
    proc = 1
    # 중요도와 순서를 저장한 queue 초기 생성
    queue = []
    for idx, priority in enumerate(priorities):
        queue.append((priority, idx))

    while queue:
        # 현재 큐의 최댓값을 저장
        top = max(queue)
        # 큐에서 하나 빼서 저장
        now = queue.pop(0)

        # 현재의 중요도가 중요도가 제일 높은 것이 아니라면 다시 큐에 저장.
        if now[0] != top[0]:
            queue.append(now)
        # 현재의 중요도가 제일 높은 중요도라면 실행.
        elif now[0] == top[0]:
            # 실행한 뒤 location이 지정한 프로그램이라면 몇 번째 순서로 실행됐는지 반환
            if now[1] == location:
                return proc
            proc += 1

'''
def solution(priorities, location):
    answer = [0] * len(priorities)
    proc = 1
    queue = []
    for idx, priority in enumerate(priorities):
        queue.append((priority, idx))

    while queue:
        top = max(queue)
        now = queue.pop(0)

        if now[0] != top[0]:
            queue.append(now)
        elif now[0] == top[0]:
            answer[now[1]] = proc
            proc += 1

    return answer[location]
'''


print(solution([2, 1, 3, 2], 2))