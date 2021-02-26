# DP: 정수 삼각형
def solution(triangle):
    maxDepth = len(triangle)
    dp = [ [0]*maxDepth for i in range(maxDepth) ]
    dp[0][0] = triangle[0][0]
    
    for depth in range(1, maxDepth):
        # left
        dp[depth][0] = dp[depth-1][0] + triangle[depth][0]
        # right
        dp[depth][depth] = dp[depth-1][depth-1] + triangle[depth][depth]
        
        for index in range(1, depth):
            dp[depth][index] = max( dp[depth-1][index], dp[depth-1][index-1] ) + triangle[depth][index]

    return max( dp[depth] )