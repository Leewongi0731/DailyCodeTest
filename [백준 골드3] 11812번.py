# 11812번: K진 트리
def sol(n1, n2, K):
    # 그래프를 그려보며 확인해보면, 
    # n1의 부모 번호는 항상 (n1+K-2) // K 인 것을 알 수 있음
    if n1==n2: return 0
    elif n1 > n2:return sol( (n1+K-2) // K, n2, K ) + 1
    else: return sol( n1, (n2+K-2) // K, K ) + 1
################################################################
N, K, Q = list(map(int, input().split()))
querys = [ list(map(int, input().split())) for i in range(Q) ]

if K==1:
    for n1, n2 in querys:
        print( abs(n1-n2) )
else:
    for n1, n2 in querys:
        print( sol( n1, n2, K ) )