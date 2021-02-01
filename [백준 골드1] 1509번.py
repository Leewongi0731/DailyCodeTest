# 1509번: 팰린드롬 분할

def getPalindromeTable(datas):
    n = len(datas)
    table = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][i] = True

    for i in range(n - 1):
        if datas[i] == datas[i + 1]:
            table[i][i + 1] = True

    for k in range(2, n):
        for i in range(n - k):
            if datas[i] == datas[i + k] and table[i + 1][i + k - 1]:
                table[i][i + k] = True
    return table

#######################################################################

datas = list(input())
table = getPalindromeTable(datas)

dp = [ i+1 for i in range(len(datas)) ]
for end in range(1, len(datas)): # 0에서 시작하는거 setting
    if table[0][end]:
        dp[end] = 1
        
for start in range(1, len(datas)): # 시작지점을 1부터 N까지
    for end in range( start, len(datas) ): # 끝지점을 시작지점부터 N까지
        if table[start][end]:
            dp[end] = min( dp[end], dp[start-1]+1 ) # dp[start-1]은 가장 작은 경로 값으로 설정되어 있으므로

print( dp[-1] )