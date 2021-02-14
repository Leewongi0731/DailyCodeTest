# 2021 카카오 공채: 메뉴 리뉴얼
from itertools import combinations

def solution(orders, course):
    countDict = {}
    course = sorted(course)
    for order in orders:
        order = ''.join(sorted(order))
        for num in course:
            if num > len(order): break
            for com in combinations( order, num ):
                try:
                    countDict[com] += 1
                except:
                    countDict[com] = 1
    
    maxNum = [ -1 for i in range( len(course) ) ] # 같은 길이의 값에서 가장 높은 빈도수 저장
    tmp = [ [] for i in range(len(course)) ] # 같은 길이의 값에서 높은 빈도수의 문자 리스트
    for key in countDict.keys():
        index = course.index( len(key) )
        if countDict[key] == 1: continue # 한곳에서만 나온 조합은 포함 X
        
        if maxNum[index] < countDict[key]:
            tmp[index] = [ ''.join(key) ]
            maxNum[index] = countDict[key]
        elif maxNum[index] == countDict[key]:
            tmp[index].append( ''.join(key) )
    
    answer = []
    for i in range( len(course) ):
        if maxNum[i] != -1: answer += tmp[i]
    answer.sort()
    
    return answer