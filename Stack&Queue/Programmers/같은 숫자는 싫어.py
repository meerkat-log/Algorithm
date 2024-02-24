# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    idx = 0

    # 처음 베열에 아무것도 없을 때는 arr의 첫번째 값 저장
    answer.append(arr[0])

    for i in range(len(arr)):
        # 연속된 값이 아니라면 추가하고  answer의 인덱스를 하나 늘림
        if arr[i] != answer[idx]:
            answer.append(arr[i])
            idx += 1

    return answer


print(solution([4,4,4,3,3]))