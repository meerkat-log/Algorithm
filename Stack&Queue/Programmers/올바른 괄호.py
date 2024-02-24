# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []

    # 괄호를 하나씩 가져와서 stack에 추가.
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            # stack에 )가 없는데 나오면 False 반환
            if not stack:
                return False
            stack.pop()

    # stack에 아무값이 없어야 True
    return not stack

print(solution(")()("))