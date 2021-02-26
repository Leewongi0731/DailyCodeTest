# DP: 도둑질
def solution(money):
    # count / 첫인자 선택 여부
    dp = [ [0, 0] for i in range(len(money) + 4) ]
    moneyLen = len(money)
    
    for i in range( moneyLen-2, 1, -1 ): # 첫 인자가 선택되었다면, 두번째, 마지막 인자는 선택 불가
        dp[i][True] = max( money[i] + dp[i+2][True], dp[i+1][True] )
            
    for i in range( moneyLen-1, 0, -1 ):
        dp[i][False] = max( money[i] + dp[i+2][False], dp[i+1][False] )
    
    answer = max( 
        money[0] + dp[2][True],
        dp[1][False]
    )
    
    return answer