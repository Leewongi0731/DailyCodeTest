# 1439번: 뒤집기
S = list(input())
changeCount = 0
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        changeCount += 1
        
if changeCount % 2 == 1:
    print( changeCount // 2 + 1 )
else:
    print( changeCount // 2 )