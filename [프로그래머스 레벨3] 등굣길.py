# DP: 등굣길
def solution(m, n, puddles):
    table = [ [ 0 for i in range(m+1) ] for i in range(n+1) ]
    for j, i in puddles:
        table[i][j] = -1
    
    for i in range(1, n+1):
        if table[i][1] == -1: break
        table[i][1] = 1
    for j in range(1, m+1):
        if table[1][j] == -1: break
        table[1][j] = 1
    
    for i in range(2, n+1):
        for j in range(2, m+1):
            if table[i][j] == -1: continue
            
            top = table[i-1][j]
            left = table[i][j-1]
            
            if top==-1 and left==-1: table[i][j] = 0
            elif top==-1: table[i][j] = left
            elif left==-1: table[i][j] = top
            else: table[i][j] = left + top
                
            table[i][j] %= 1000000007
        
    return table[n][m]