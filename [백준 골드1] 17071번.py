# 17071번: 숨바꼭질 5
N, K = list(map(int, input().split()))

kpos = [K]
maxSec = 1
while True:
    if kpos[-1]+maxSec <= 500000:
        kpos.append( kpos[-1]+maxSec )
        maxSec+=1
    else:
        break

# 해당 위치 짝수초 방문/홀수초 방문
# 아이디어 : 현재 위치는 2초뒤에 다시 돌아올수 있다. ( 앞/뒤 이동 or 뒤/앞 이동 )
firstVistedTime = [ [-1, -1] for i in range(500001) ] 
firstVistedTime[N][0] = 0
sec = 0
npos = set()
npos.add(N)
findFlag=False
while sec < maxSec:
    if firstVistedTime[ kpos[sec] ][ sec%2 ] != -1: # 이전에 방문한 기록이 있다!
        findFlag=True
        break
    
    nextPos = set()
    nextSecFlag = (sec+1) % 2
    for pos in npos:
        if pos-1 >=0 and firstVistedTime[pos-1][nextSecFlag]==-1:
            firstVistedTime[pos-1][nextSecFlag]=sec+1
            nextPos.add( pos-1 )
        if pos+1 <= 500000 and firstVistedTime[pos+1][nextSecFlag]==-1:
            firstVistedTime[pos+1][nextSecFlag]=sec+1
            nextPos.add( pos+1 )
        if pos*2 <= 500000 and firstVistedTime[pos*2][nextSecFlag]==-1:
            firstVistedTime[pos*2][nextSecFlag]=sec+1
            nextPos.add( pos*2 )
    npos = nextPos
    sec += 1

if findFlag: print( sec )
else: print(-1)