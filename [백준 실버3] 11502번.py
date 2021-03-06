# 11502번: 세 개의 소수 문제
from bisect import bisect_left

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
########################################################################
primes = prime_list(1000)

T = int(input())
for _ in range(T):
    K = int(input())
    index = bisect_left( primes, K )
    
    result = []
    for firstIndex in range(index):
        for secondIndex in range(firstIndex, index):
            lastV = K - primes[firstIndex] - primes[secondIndex]
            if lastV <= 1: break
                
            lastIndex = bisect_left( primes, lastV )
            if primes[lastIndex]==lastV:
                result = sorted( [ primes[firstIndex], primes[secondIndex], primes[lastIndex] ] )
                break
                
        if result!=[]: break
            
    if result==[]: print(0)
    else: print( ' '.join( map(str, result) ) )