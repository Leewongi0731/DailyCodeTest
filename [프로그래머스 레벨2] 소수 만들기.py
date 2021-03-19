# Summer/Winter Coding: 소수 만들기
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하, 중복 X
from itertools import combinations

def getPrime(n):
    check = [ True for i in range(n+1) ]
    check[0] = check[1] = False
    
    for i in range(n+1):
        if check[i] == True:
            j = 2
            while i*j <= n:
                check[ i*j ] = False
                j += 1
    return check
        

def solution(nums):
    primeCheck = getPrime(3000)
    
    answer = 0
    for com in combinations( nums, 3 ):
        s = sum(com)
        if primeCheck[s] == True: answer += 1

    return answer