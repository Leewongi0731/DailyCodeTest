# 9252번: LCS 2
A = input()
B = input()

dp = [[ 0 for i in range(len(A) + 1) ] for j in range(len(B) + 1) ]

for i in range(1, len(B) + 1):
    target = B[i-1]
    for j in range(1, len(A) + 1):
        if A[ j - 1 ] == target:
            dp[ i ][ j ] = dp[i-1][j-1] + 1
        else:
            dp[ i ][ j ] = max( dp[i-1][j], dp[i][j-1] )


if dp[ len(B) ][ len(A) ] == 0:
    print( 0 )
else:
    LCSLength = dp[ len(B) ][ len(A) ]
    LCSWord = ""
    tmp = dp[ len(B) ][ len(A) ]
    for i in range( len(B), 0, -1 ):
        for j in range( len(A), 0, -1 ):
            if tmp == dp[ i ][ j ] and dp[ i ][ j ] > dp[i][j-1]:
                if dp[ i ][ j ] == dp[ i-1 ][ j ]: # 해당 문자는 공통 문자열이 아님
                    break
                LCSWord =  A[ j-1 ] + LCSWord
                tmp -= 1
                break
    print( LCSLength )
    print( LCSWord )