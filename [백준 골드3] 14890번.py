# 14890번: 경사로
def flatCheck( line ):
    global N, L
    
    i = 1
    flatLen = 1
    while i < N:
        if line[i] == line[i-1]: flatLen+=1
        elif abs(line[i]-line[i-1]) == 1 :
            # 오르막길
            if line[i] > line[i-1]:
                # 이전에 경사로를 설치 할 길이가 안됨
                if flatLen<L: return False
                flatLen = 1
            # 내리막길
            else:
                afterFlatLen = 0
                for nextIndex in range( i, min(i+L, N) ):
                    if line[i]==line[nextIndex]: afterFlatLen+=1
                    else: break

                    if afterFlatLen==L: break

                if afterFlatLen==L:
                    i = nextIndex
                    flatLen = 0
                else: return False 
                    
        else:
            # 2칸이상 차이나면 설치 불가
            return False
        
        i+=1
        
    return True
########################################################################
N, L = list(map(int, input().split()))
table = [ list(map(int, input().split())) for i in range(N) ]

result = 0
for i in range(N):
    if flatCheck( table[i] ):result+=1
        
    col = [ table[j][i] for j in range(N) ]
    if flatCheck( col ):result+=1
print( result )