def solution(triangle):
    # triangle 리스트의 0번인 가장 맨 윗 값은 변경될 필요가 없어 인덱스 1번부터 마지막 인덱스까지 반복
    for i in range(1, len(triangle)):
        # triangle은 2차원 배열이기 때문에 하나의 가져온 리스트의 길이를 다시 구하여 그 길이만큼 또 반복
        for j in range(len(triangle[i])):
            # [i][0]의 위치에 있는 값은 연결된 값이 [i-1][0] 밖에 없어 해당 값과 현재 위치의 값인 [i][j]를 더한 값으로 업데이트
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]
            # [i][-1]의 위치에 있는 값도 연결된 값이 [i-1][j-1] 밖에 없어 해당 값과 현재 위치의 값인 [i][j]를 더한 값으로 업데이트
            elif j == len(triangle[i])-1:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            # 맨 처음과 맨 끝 값이 아니라면 두 개의 상위 값이 존재하여 둘 중에서 더 큰 값으로 더하여 현재 [i][j]를 업데이트
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j], triangle[i-1][j-1])

    # 값이 모두 업데이트 되었다면 그 중에서 가장 큰 값을 반환
    return max(triangle[-1])



print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))