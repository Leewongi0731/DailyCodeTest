# 12850번: 본대 산책2
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) % 1000000007 for B_col in zip(*B)] for A_row in A]

def getDp(i):
    if i in dp.keys():
        return dp[i]
    else:
        if i % 2 == 1:
            dp[i] = productMatrix( getDp(i//2), getDp(i//2+1) )
        else:
            dp[i] = productMatrix( getDp(i//2), getDp(i//2) )
        return dp[i]
##########################################################################################
dp = { 1: [[0,1,1,0,0,0,0,0], 
          [1,0,1,1,0,0,0,0],
          [1,1,0,1,1,0,0,0],
          [0,1,1,0,1,1,0,0],
          [0,0,1,1,0,1,0,1],
          [0,0,0,1,1,0,1,0],
          [0,0,0,0,0,1,0,1],
          [0,0,0,0,1,0,1,0]] }

D = int(input())

result = getDp(D)
print( result[0][0] )