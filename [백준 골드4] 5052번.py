# 5052번: 전화번호 목록
from bisect import bisect_left

t = int(input())
for _ in range(t):
    n = int(input())
    
    datas = [ input() for i in range(n) ]
    datas = sorted( datas )
    
    #  각 '0' ~ '9'로 시작하는 숫자의 첫 index
    eachNumIndex = [ bisect_left(datas, str(num)) for num in range(10) ] + [n]
    
    result = "YES"
    for num in range(10):
        checkData = datas[ eachNumIndex[num] : eachNumIndex[num+1] ]
        if len(checkData) <= 1: continue
        
        for i in range( 1, len(checkData) ):
            beforData = checkData[i-1]
            nowData = checkData[i]
            if nowData[:len(beforData)] == beforData:
                result="NO"
                break
                
        if result=="NO": break
            
    print( result )