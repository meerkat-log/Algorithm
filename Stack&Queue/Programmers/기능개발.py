# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    count = 0

    # progresses가 존재하면 계속해서 덧셈 진행
    while progresses:
        # progreeses의 첫번째 값이 100이 넘어가면 개발이 완료되어 출시 가능.
        if progresses[0] >= 100:
            # 출시 가능한 프로그램의 개수를 하니씩 더하다가 아직 미개발된 프로그램이 있을 시 이전까지만 출시.
            count += 1
            del progresses[0]
            del speeds[0]
        elif count != 0:
            answer.append(count)
            count = 0
        else:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

    answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))