# 9177번: 단어 섞기
from collections import deque

N = int( input() )
for i in range(N):
    word1, word2, question = input().split()
    if word1 + word2 == question or word2 + word1 == question:
        print( "Data set "+ str(i+1) +": yes" )
        continue
    
    possible = False
    queue = deque()
    queue.append( [0, 0, 0] )
    while queue:
        index1, index2, indexQ = queue.pop()
        
        if indexQ == len(question):
            possible = True
            break
        if index1 == len(word1):
            if question[indexQ:] == word2[index2:]:
                possible = True
                break
            else:  break
        if index2 == len(word2):
            if question[indexQ:] == word1[index1:]:
                possible = True
                break
            else:  break
        
        if word1[ index1 ] == word2[ index2 ] == question[ indexQ ]:
            queue.append( [index1+1, index2, indexQ+1] )
            queue.append( [index1, index2+1, indexQ+1] )
        elif word1[ index1 ] == question[ indexQ ]:
            queue.append( [index1+1, index2, indexQ+1] )
        elif word2[ index2 ] == question[ indexQ ]:
            queue.append( [index1, index2+1, indexQ+1] )
        
    if possible:
        print( "Data set "+ str(i+1) +": yes" )
    else:
        print( "Data set "+ str(i+1) +": no" )