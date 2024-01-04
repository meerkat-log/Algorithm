def solution(N, number):
    # N이 1개 사용됐을 때부터 8개 사용됐을 때를 저장하기 위한 리스트
    all_case = []

    # N의 사용 개수가 8을 초과하면 -1을 반환하기 때문에 1부터 8까지만으로 반복문 제어
    for count in range(1, 9):
        # 현재 사용된 N의 개수에 따른 연산 결과를 저장하기 위한 임시 리스트
        temp_case = []
        # N이 5라고 가정하고 4개를 사용했다면 5555도 가능하기 때문에 이를 추가하기 위한 코드
        temp_case.append(int(str(N) * count))
        # 현재 count가 4라면 all_case 리스트는 0~2까지의 인덱스가 존재한다.
        # 왜냐하면 N이 4개가 사용된다면 1 + 3, 2 + 2, 3 + 1이 가능하기 때문이다.
        # 인덱스가 0일 때는 1개, 1일 때는 2개, 2일 때는 3개가 사용된 결과가 저장되어 있다.
        # 따라서 이를 조합하여 N이 4개가 사용된 결과를 생성하게 되는 것이다.
        # 그렇기 때문에 count-1까지로 하여 반복을 하고 모든 조합을 생성한다.
        for i in range(count-1):
            print(count, i, -(i+1))

            # n1은 all_case[i]의 값을 가져온다.
            # 즉, 리스트의 0번 인덱스부터 접근한다.
            for n1 in all_case[i]:
                # n2는 all_case[-(i+1)]의 값을 가져온다.
                # 즉, 리스트의 맨 마지막 인덱스부터 접근한다.
                for n2 in all_case[-(i+1)]:
                    # 사칙 연산을 진행
                    temp_case.append(n1 + n2)
                    temp_case.append(n1 - n2)
                    temp_case.append(n1 * n2)
                    # n2가 0일수도 있기 때문에 0으로는 나눗셈을 할 수 없어 0일 때만 나눗셈 진행
                    if n2 != 0:
                        temp_case.append(n1 // n2)

        # 구해야 하는 결과값인 number가 temp_case에 있으면 bottom-up 방식의 dp 방식이므로 최소값이 된다.
        # 따라서 현재의 count 값을 return 한다.
        if number in temp_case:
            return count
        # number의 값이 없다면 N의 1 증가하여 계산을 해야 하기 때문에 set()을 사용하여 중복된 값을 제거
        # 중복된 값을 제거한 후 all_case에 현재의 temp_case값을 추가한다.
        temp_case = list(set(temp_case))
        all_case.append(temp_case)
        print(all_case)

    return -1

print("정답:", solution(8, 5800))