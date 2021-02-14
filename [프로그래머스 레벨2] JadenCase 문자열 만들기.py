# 연습문제: JadenCase 문자열 만들기
def solution(s):
    answer = ''
    for splitS in s.split(' '):
        if splitS == '': 
            answer += " "
        else:
            addS = splitS[0].upper() + splitS[1:].lower()
            answer += addS + ' '
    return answer[:-1]