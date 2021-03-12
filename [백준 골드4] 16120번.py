# 16120번: PPAP
from collections import deque

datas = list(input())
stack = deque()
for data in datas:
    stack.append( data )

    while len(stack) >= 4:
        if stack[-1] == 'P' and stack[-2] == 'A' and stack[-3] == 'P' and stack[-4] == 'P':
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append( 'P' )
        else:
            break
    print( stack )
if stack==deque(['P']):print( 'PPAP' )
else: print( 'NP' )