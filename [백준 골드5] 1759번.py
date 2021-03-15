# 1759번: 암호 만들기
from itertools import combinations

L, C = list(map(int, input().split()))
datas = input().split()
datas = sorted( datas )

consonants = ['a', 'e', 'i', 'o', 'u']
consonantCheck = [  ]
for consonant in consonants:
    if consonant in datas: consonantCheck.append( True )
    else: consonantCheck.append( False )
        
for com in list(combinations( datas, L ) ):
    consonantsCount = 0
    if consonantCheck[0]==True and 'a' in com: consonantsCount+=1
    if consonantCheck[1]==True and 'e' in com: consonantsCount+=1
    if consonantCheck[2]==True and 'i' in com: consonantsCount+=1
    if consonantCheck[3]==True and 'o' in com: consonantsCount+=1
    if consonantCheck[4]==True and 'u' in com: consonantsCount+=1
    
    if consonantsCount >= 1 and L-consonantsCount>=2:
        print( ''.join(com) )