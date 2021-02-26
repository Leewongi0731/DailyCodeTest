# DFS/BFS: 단어 변환
from collections import deque

def convertCheck( word1, word2, wordLen ):
    flag = False
    for i in range( wordLen ):
        if word1[i] != word2[i]:
            if flag==False: flag=True
            else: return False
    return True

def solution(begin, target, words):
    wordLen = len(begin)
    words = [begin] + words
    words = list(set(words))
    
    
    convert = [ [False]*len(words) for i in range( len(words) ) ]
    for index1 in range( len(words) ):
        for index2 in range( index1+1, len(words) ):
            word1, word2 = words[index1], words[index2]
            convert[index1][index2] = convert[index2][index1] = convertCheck( word1, word2, wordLen )
    
    
    visited = [ False for i in range( len(words) ) ]
    startIndex = words.index( begin )
    visited[startIndex] = True
    queue = deque()
    queue.append( [begin, startIndex, 0] ) # value, index, count
    while queue:
        word, index, count = queue.popleft()
        
        if word==target: return count
        
        for nextIndex in range( len(words) ):
            if convert[index][nextIndex]==True and visited[nextIndex]==False:
                visited[nextIndex]=True
                queue.append( [ words[nextIndex], nextIndex, count+1 ] )
    return 0