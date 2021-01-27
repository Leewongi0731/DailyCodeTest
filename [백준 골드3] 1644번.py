# 1644번: 소수의 연속합
def prime_list(n):
    sieve = [True] * n
    
    m = int( n ** 0.5  )
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
                
    return [i for i in range(2, n) if sieve[i] == True]
###########################################################################
N = int(input())
result = 0
if N != 1:
    prime = prime_list( N+1 )

    pre, net= 0, 0
    rangeSum = prime[0]

    if prime[-1] == N: result += 1

    while pre <= net and net < len(prime)-1:
        if rangeSum == N: result += 1        
        if rangeSum <= N:
            net += 1
            rangeSum += prime[net]
        elif rangeSum > N:
            rangeSum -= prime[pre]
            pre += 1

print(result)