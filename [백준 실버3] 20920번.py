# 20920번: 영단어 암기는 괴로워
# 2021 ICPC Sinchon Winter Algorithm Camp Contest - 초급 : A 
from collections import Counter

N, M = list(map(int, input().split()))

data = []
for i in range(N):
    word = input()
    if len(word) >= M:
        data.append( word )
        
counter = Counter( data )
data = []
for key, c in counter.items():
    data.append( [c, len(key), key] )

for c, l, word in sorted( data, key=lambda x: (-x[0], -x[1], x[2]) ):
    print( word )