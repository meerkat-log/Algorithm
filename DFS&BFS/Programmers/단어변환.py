# https://school.programmers.co.kr/learn/courses/30/lessons/43163

# 단어에서 한글자씩 비교하는 함수
def compareWord(word1, word2):
    count = 0
    
    # 단어의 길이는 같기 때문에 단어의 글자수 만큼 반복
    for i in range(len(word1)):
        # 같은 위치의 문자가 다르면 카운트
        if word1[i] != word2[i]:
            count = count + 1

    # 카운트된 수가 1이면 1글자만 다른 것으로 인식하여 True 반환
    # 1이 아닌 수일 때는 False 반환
    if count == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    # 방법이 다양하게 있을 수 있고 최소 몇 단계를 거쳐야 하는지를 알아야 하기 때문에 answer 리스트 선언 
    answer = []
    # 단어의 개수만큼 방문했는지 기록하기 위한 visited 리스트 선언
    visited = [False] * len(words)

    def dfs(count, now, target):
        # 단어가 일치했을 때 count 값 저장
        if now == target:
            answer.append(count)

        for index, word in enumerate(words):
            # 단어를 하나씩 가져와서 현재의 단어와 비교하고 방문하지 않은 곳이면 DFS 진행
            if compareWord(now, word) and visited[index] == False:
                visited[index] = True
                dfs(count=count+1, now=word, target=target)
                # 다른 방법도 있을 수 있기 때문에 visited를 다시 False로 변경
                visited[index] = False

    # target이 words 리스트에 없다면 0 반환
    if target not in words:
        answer.append(0)
    else:
        dfs(count=0, now=begin, target=target)

    answer.sort()
    return answer[0]

print(solution(begin="hit", target="cog", words=["hot", "dot", "dog", "lot", "log"]))