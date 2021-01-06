# 9328번: 열쇠
from collections import deque

T = int( input() )
for _ in range(T):
    H, W = list(map(int, input().split()))
    map_ = [ [] for i in range(H) ]
    for i in range(H):
        map_[i] = list( input() )
    
    # set key
    keys = input()
    key = { chr( ord('A') + i ) : 0 for i in range(26) }
    keyCount = 0
    if keys != '0':
        for k in keys:
            key[ chr( ord(k) - 32 ) ] = 1
            keyCount += 1
            
    queue = deque()
    block = { chr( ord('A') + i ) : set() for i in range(26) }
    # set queue
    for w in range(W): 
        if ord('A') <= ord(map_[0][w]) and ord(map_[0][w]) <= ord('Z'):
            if key[map_[0][w]] == 0: # 문이고 못 들어간다면
                block[map_[0][w]].add( (0, w) )
            else:
                queue.append( [0, w] )
        elif map_[0][w] == '.' or map_[0][w] == '$':
            queue.append( [0, w] )
            
        if ord('A') <= ord(map_[H-1][w]) and ord(map_[H-1][w]) <= ord('Z'):
            if key[map_[H-1][w]] == 0: # 문이고 못 들어간다면
                block[map_[H-1][w]].add( (H-1, w) )
            else:
                queue.append( [H-1, w] )
        elif map_[H-1][w] == '.' or map_[H-1][w] == '$':
            queue.append( [H-1, w] )

    for h in range(H):
        if ord('A') <= ord(map_[h][0]) and ord(map_[h][0]) <= ord('Z'):
            if key[map_[h][0]] == 0: # 문이고 못 들어간다면
                block[map_[h][0]].add( (h, 0) )
            else:
                queue.append( [h, 0] )
        elif map_[h][0] == '.' or map_[h][0] == '$':
            queue.append( [h, 0] )
            
        if ord('A') <= ord(map_[h][W-1]) and ord(map_[h][W-1]) <= ord('Z'):
            if key[map_[h][W-1]] == 0: # 문이고 못 들어간다면
                block[map_[h][W-1]].add( (h, W-1) )
            else:
                queue.append( [h, W-1] )
        elif map_[h][W-1] == '.' or map_[h][W-1] == '$':
            queue.append( [h, W-1] )

    # visited -> keyCount로 Check
    dp = [ [-1 for i in range(W)] for j in range(H) ]
    mx = [1, -1, 0, 0]
    my = [0, 0, 1, -1]
    result = 0
    while queue:
        h, w = queue.popleft()
        if map_[h][w] == '$':
            result += 1
            map_[h][w] = '.'
        elif ord('a') <= ord(map_[h][w]) and ord(map_[h][w]) <= ord('z'):
            if key[ chr( ord(map_[h][w]) - 32 ) ] == 0:
                queue += block[ chr( ord(map_[h][w]) - 32 ) ]
                block[ chr( ord(map_[h][w]) - 32 ) ] = set()
                key[ chr( ord(map_[h][w]) - 32 ) ] = 1
                keyCount += 1
            else:
                map_[h][w] = '.'
        elif ord('A') <= ord(map_[h][w]) and ord(map_[h][w]) <= ord('Z'):
            map_[h][w] = '.'

        dp[ h ][ w ] = keyCount

        for i in range( 4 ):
            mh = h + mx[i]
            mw = w + my[i]

            if mh >= 0 and mh < H and mw >= 0 and mw < W and map_[mh][mw] != '*': # 갈수는 경우 제외
                if ord('A') <= ord(map_[mh][mw]) and ord(map_[mh][mw]) <= ord('Z') and key[map_[mh][mw]] == 0: # 문이고 못 들어간다면
                    block[map_[mh][mw]].add( (mh, mw) )
                    continue
                if dp[mh][mw] >= keyCount:
                    continue
                    
                dp[mh][mw] = keyCount # < 미리 check하지 않으면 중복해서 queue에 들어가기 때문에 시간초과 발생
                queue.append( [mh, mw] ) 
    print( result )