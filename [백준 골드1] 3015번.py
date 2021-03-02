# 3015번: 오아시스 재결합
import sys

N = int(input())

stack=[]
result=0
for _ in range(N):
    h=int(sys.stdin.readline())
    
    # stack의 top은 항상 가장 작은 값이여야 함.
    while stack:
        if stack[-1][0]>=h: break
        else:
            # 새로운 h보다 작은 값들은 h이후에 새로운 사람을 볼 수 없고, h까지만 볼 수 있음
            # ex) 6 6 7 8 9 두번째 7이 들어올때 앞의 2개의 6은 지금 들어온 7까지만 볼 수 있음
            result+=stack[-1][1]
            stack.pop()
    
    if stack==[]:
        stack.append([h,1])
    else:
        if stack[-1][0]==h:
            # top값과 새로운 h가 같다면, 기존 top 갯수만큼 추가될 수 있음
            result+=stack[-1][1]
            stack[-1][1] += 1
            
            # stack에 h말고 다른 값이 있다면, 그 값은 h보다 클 것이며, h는 최대 사람까지 볼 수 있다.
            # ex) 7 7 6 6 (마지막 6은 최대 2번째 7까지만 볼 수 있음, 첫번째 7은 두번째 7에 가려져 보이지 않음)
            if len(stack)!=1: result+=1
        else:
            # 새로운 h가 기존 top보다 작다면, 해당 위치에서 뒤로는 단 한개밖에 보이지 않음
            # ex) 7 7 6 (마지막 6은 최대 2번째 7까지만 볼 수 있음, 첫번째 7은 두번째 7에 가려져 보이지 않음)
            stack.append([h,1]) 
            result+=1
print(result)