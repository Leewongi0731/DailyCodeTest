# 1256번: 사전
def initFactorial( n ):
    if n > 1: factorial[n] *= n * initFactorial(n-1)
    return factorial[n]

def nCr(n,r):
    return factorial[n] // factorial[r] // factorial[n-r]

factorial = [ 1 for i in range(201) ]
initFactorial(200)
##############################################################################
N, M, K = list(map(int, input().split()))

if nCr( N+M, N ) < K:
    # N개의 a와 M개의 z로 K개를 만들 수 없을 경우
    print(-1)
else:
    # index를 맞추기 위해 K를 1감소시킴
    K -= 1
    aCount = N
    zCount = M
    answer = ""
    
    while K:
        # 현재의 answer 바로 뒤에 붙을 값이 'a'인지, 'z'인지 구별하기 위해 그 뒤로 몇 개의 경우가 존재하는지 확인
        afterCount = nCr(aCount+zCount-1, aCount-1)
        
        if afterCount <= K:
            # z 확정
            K -= afterCount
            answer += 'z'
            zCount -= 1
            if zCount == 0: break
            
        else:
            # a 확정
            answer += 'a'
            aCount -= 1
            if aCount == 0: break
                
    answer += 'a'*aCount
    answer += 'z'*zCount
    print( answer )