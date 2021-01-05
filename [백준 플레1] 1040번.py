# 1040번: 정수

# https://github.com/encrypted-def/BOJ/blob/master/1040.py
# 바킹독님 풀이.
def numkind(N):
    if type(N) == int:
        N = str(N)
    return len(set(list(N)))

def numList(N):
    if type(N) == int:
        N = str(N)
    tmpL = [0]*10
    for c in N:
        tmpL[ord(c)-ord('0')] = 1
    unused = []
    used = []
    for i in range(10):
        if tmpL[i] == 0: unused.append(i)
        else: used.append(i)
    return unused,used

def concat(L):
    s = ''
    for c in L:
        s += str(c)
    return s
def solve(N,K): 
    N = str(N)
    if numkind(N) == K:
        print(N)
        return 0
    for prefix_i in range(len(N)-1, -1,-1):
        for prefix_last in range(ord(N[prefix_i])-48+1,10):
            prefix = N[:prefix_i]+chr(prefix_last+48)
            leftnum = K-numkind(prefix) # 추가되어야 하는 종류의 갯수
            leftlen = len(N)-prefix_i-1 # leftlen만큼의 길이가 추가되어야 함
            if leftnum < 0 or leftnum > leftlen: continue # 잘 조정해도 절대 수의 종류를 K개로 만들 수 없다면
            unused,used = numList(prefix)
            if leftnum == 0:
                print(prefix+str(used[0])*leftlen)
                return 0
            print(prefix+'0'*(leftlen-leftnum)+concat(unused[:leftnum]))
            return 0
    # 여기에 도달했다는 것은 N자리로는 절대 완성이 불가능해서 N+1자리가 필요한 상황
    N = max(K,len(N)+1)
    print("1"+"0"*(N-K+1)+"23456789"[:K-2])

N,K=map(int,input().split())
solve(N,K)


'''
# 기존 내 풀이 : 계속 메모리 초과. bitCheck를 List가 아닌 Bit로 해봐야 할 것 같음

import sys
sys.setrecursionlimit(10**8) 

def checkDownCount( bitCheck, startIndex ): 
    # count 수가 K보다 클때 사용
    # 앞에서 부터 bit Check를 통해 K보다 커지는 COUNT를 찾고, 해당 지점을 앞에서 나온 숫자로 대처할 수 있는지 판단.
    # example : 11221223345 3  -> 112212233 까지는 count:3 -> 4나오는 지점을 startIndex
    # 앞에서 나온 [1,2,3] 은 모두 4보다 작음. 11221223345 -> 11221223400 -> 11221224111
    # example : 55225223345 3 -> 552252233 까지는 count:3 -> 4나오는 지점을 startIndex
    # 앞에서 나온 [2,3,5] 중 5는 4보다 큼. 55225223345 -> 55225223352
    global listN, K
    
    possibleValue = -1
    for i in range(9, -1, -1):
        if bitCheck[i] == 1 and listN[ startIndex ] < i:
            possibleValue = i
    
    print("Dwon", listN, K, bitCheck, startIndex, possibleValue ) 
    
    if possibleValue == -1:
        listN[ startIndex-1 ] += 1
        for i in range( startIndex, len(listN) ):
            listN[i] = 0
            
        bitCheck = [ 0 for i in range(10) ]
        count = 0
        for i, n in enumerate( listN ):
            if bitCheck[ n ] == 0:
                bitCheck[n] = 1
                count += 1
            if count > K:
                bitCheck[n] = 0
                return checkDownCount( bitCheck, i )
        return int(''.join( map(str, listN)))
    else:
        minValue = [i for i in range(9, -1, -1) if bitCheck[i] == 1][-1]
                
        listN[ startIndex ] = possibleValue
        for i in range( startIndex+1, len(listN) ):
            listN[i] = minValue
        return int(''.join( map(str, listN)))
    
def checkUpCount( ):
    # count 수가 K보다 작을때 사용
    # 뒤부터 중복되는 수를 찾고 해당수부터 뒷 부분을 새로운 check안된 새로운 BIT로 바꿔가며 테스트
    # example : 1122332245 7
    # leftBitCheck : [1:0, 2:2, 3:4]  / upIndex : 7 / rightBitCheck = [2:7, 4:8, 5:9]
    # leftBitCheck에 없으면 -> possibleList : [ 0, 4, 5, 6, 7, 8, 9 ]
    # listN[ upIndex ] = 2 > 4 : 1122332245 -> 1122332"405"
    # 다시 leftBitCheck, upIndex, rightBitCheck를 update하고 count가 K랑 같아질때 out.
    global listN, K
    leftBitCheck = [ -1 for i in range(10) ]
    rightBitCheck = [ -1 for i in range(10) ]
    upIndex = -1
    for i in range( len(listN) -1, -1, -1):
        n = listN[i]
        if upIndex == -1:
            if rightBitCheck[ n ] == -1:
                rightBitCheck[n] = i
            else:
                upIndex = rightBitCheck[ n ]
                for j in range( i, upIndex ):
                    rightBitCheck[ listN[j] ] = -1
                    leftBitCheck[ listN[j] ] = j
                rightBitCheck[ n ] = upIndex
        else:
            leftBitCheck[ n ] = i

            
    k = 0
    while k < K:
        possibleList = [ i for i in range(10) if leftBitCheck[i] == -1 ]
        
        if listN[ upIndex ] > possibleList[-1]: # upindex에서 올림
            add = 10 - listN[ upIndex ]
            upValue = pow(10, len( listN ) - upIndex - 1 ) * add
            N = int(''.join( map(str, listN))) + upValue
            N = list(map(int, str(N)))
            # update leftBitCheck
            leftBitCheck = [ -1 for i in range(10) ]
            if len(N) > len(listN):
                upIndex += 1
            for i in range( upIndex-1, -1, -1 ):
                leftBitCheck[ N[i] ] = i
            listN = N
            possibleList = [ i for i in range(10) if leftBitCheck[i] == -1 ]
        
        # update value
        for p in possibleList:
            if listN[ upIndex ] < p:
                listN[ upIndex ] = p
                break
        possibleList.remove(p)
            
        # update RightBitCheck
        listN[upIndex+1:] = possibleList[0 : len(listN)-upIndex-1 ]
        rightBitCheck = [ -1 for i in range(10) ] 
        for i in range( upIndex, len(listN) ):
            if rightBitCheck[ listN[i] ] == -1:
                rightBitCheck[ listN[i] ] = i
        
        # new upIndex
        for i in range( upIndex-1, -1, -1 ):
            if leftBitCheck[ listN[ i ] ] != i: # 중복
                upIndex = i
                break
            else:
                rightBitCheck[ listN[ i ] ] = i
                leftBitCheck[ listN[ i ] ] = -1
        
        # set k
        k = 0
        for i in range(10):
            if leftBitCheck[i] != -1 or rightBitCheck[i] != -1:
                k += 1

    return int(''.join( map(str, listN))) 

def sol( ):
    global listN, K
    print("MAIN", listN, K)
    bitCheck = [ 0 for i in range(10) ]
    count = 0

    for i, n in enumerate( listN ):
        if bitCheck[n] == 0:
            bitCheck[n] = 1
            count += 1
        if count > K:
            bitCheck[n] = 0
            return checkDownCount( bitCheck, i )
    
    if K == count:
        return int(''.join( map(str, listN)))
    elif K > count and len( listN ) < K: # 길이 자체가 안된다면 
        return [1, 10, 102, 1023, 10234, 102345, 1023456, 10234567, 102345678, 1023456789][ K-1 ]
    elif K > count:
        return checkUpCount( )
    
################################################################################################
N, K = list(map(int, input().split()))
listN = list(map(int, str(N)))
print( sol( ) )
'''