# 9527번: 1의 개수 세기
bitSum = [ 0 for i in range(56) ]
bitSum[0] = 1
for i in range(1, 56):
    bitSum[ i ] = bitSum[ i-1 ] * 2 + pow(2, i-1)

    
bitBeforAfter = { }
tmp1 = 0
tmp2 = 0
for i in range( 55 ):
    tmp1 += bitSum[i]
    tmp2 += pow( 2, i )
    bitBeforAfter[i] = [ tmp1, tmp2 ] 
    
    
def getOneBitCount( x ):
    result = 0
    x = bin(x)[2:]
    for i in range(len(x)-1):
        result += bitSum[i]
    
    beforOneBit = 1
    afterBit = len(x)
    index = 0
    while afterBit > 1:
        index += 1
        afterBit -= 1
        
        if x[index] == '1':
            try:
                tmp = bitBeforAfter[afterBit-2]
                result += tmp[0] + ( tmp[1] + 1 ) * beforOneBit
            except: # 마지막 비트가 1
                result += beforOneBit
                
            beforOneBit += 1
            
    result += beforOneBit
        
    return result
########################################3
A, B = list(map(int, input().split()))
result = getOneBitCount(B) - getOneBitCount(A) + bin(A).count('1')
print( result )