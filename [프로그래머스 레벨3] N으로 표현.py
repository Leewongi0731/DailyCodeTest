# DP: N으로 표현
from collections import deque

def solution(N, number):
    maxSize = 1000000
    checked = [ 0 for i in range( maxSize+1 ) ]
    
    step = [ [] for i in range(10)]
    
    pastes = [0, N]
    for i in range(1, 9):
        pastes.append( pastes[-1]*10+N )
        step[i] = [ pastes[i] ]

    for count in range( 1, 9 ):
        for c in range( 1, count//2 + 1 ):
            for item1 in step[c]:
                for item2 in step[count-c]:                
                    # 더하기
                    if 0<= item1+item2 <= maxSize and checked[item1+item2]==0:
                        checked[item1+item2]=1
                        step[count].append(item1+item2)
                        
                    # 빼기1
                    if 0<= item1-item2 <= maxSize and checked[item1-item2]==0:
                        checked[item1-item2]=1
                        step[count].append(item1-item2)
                    # 빼기2
                    if 0<= item2-item1 <= maxSize and checked[item2-item1]==0:
                        checked[item2-item1]=1
                        step[count].append(item2-item1)
                        
                    # 곱하기
                    if 0<= item1*item2 <= maxSize and checked[item1*item2]==0:
                        checked[item1*item2]=1
                        step[count].append(item1*item2)

                    # 나누기1
                    if item2!=0 and 0<= item1//item2 <= maxSize and checked[item1//item2]==0:
                        checked[item1//item2]=1
                        step[count].append(item1//item2)
                    # 나누기2
                    if item1!=0 and 0<= item2//item1 <= maxSize and checked[item2//item1]==0:
                        checked[item2//item1]=1
                        step[count].append(item2//item1)

        if number in step[count]: return count

    return -1