# 연습문제: 줄 서는 방법
def solution(n, k):
    # 아이디어 : k값을 조정해가며 앞에서부터 한자리씩 값을 채워 나감
    k -= 1
    datas = [ i for i in range(1, n+1) ]
    factorials = [1, 1]
    for i in range( 2, n+1 ): factorials.append( factorials[-1]*i )
    
    answer = [ 0 for i in range(n) ]
    searchIndex = 0
    while searchIndex < n:
        # 현재위치의 값을 결정하는 것은 남은( n-searchIndex-1 ) 갯수의 factorial에 의해 index가 결정됨
        divPec = factorials[ n - searchIndex - 1 ]
        index = k // divPec
        k %= divPec
        
        # 남은 1~n중에 해당위치의 index값을 pop하여 대입함
        answer[ searchIndex ] = datas.pop( index )
        
        # 위 과정을 처리한 후, 다음 index를 탐색함
        searchIndex += 1
        
    return answer