# 20923번: 숫자 할리갈리 게임
# 2021 ICPC Sinchon Winter Algorithm Camp Contest - 초급 : D

import sys
from collections import deque

N, M = list(map(int, input().split()))
doDeck = deque()
suDeck = deque()
for _ in range(N):
    d, s = list(map(int, sys.stdin.readline().split()))
    doDeck.append( d )
    suDeck.append( s )

doField = []
suField = []
turn = 0
while turn < M:
    # 2. 그라운드에 숫자가 보이도록 내려놓는다
    if turn % 2 == 0: # do turn
        doField.append( doDeck.pop() )
    else: # su turn
        suField.append( suDeck.pop() )
    if len(doDeck) == 0 or len(suDeck) == 0: break
    
    # 3. 
    if len(doField) > 0 and len(suField) > 0 and doField[-1]+suField[-1]==5: # su Win
        for data in doField: suDeck.appendleft( data )
        for data in suField: suDeck.appendleft( data )
        suField = []
        doField = []
        
    elif ( len(doField)>0 and doField[-1]==5 ) or ( len(suField)>0 and suField[-1]==5 ): # do Win
        for data in suField: doDeck.appendleft( data )
        for data in doField: doDeck.appendleft( data )
        suField = []
        doField = []

    turn += 1
    
if len(doDeck) > len(suDeck): print( 'do' )
elif len(doDeck) < len(suDeck): print( 'su' )
else: print( 'dosu' )