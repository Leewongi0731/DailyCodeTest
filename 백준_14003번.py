# 14003번: 가장 긴 증가하는 부분 수열 5
def getInsertIndex( x ):
    start = 0
    end = len(dp) 
    
    while start < end:
        mid = ( start + end ) // 2
        if dp[ mid ] < x:
            if start == mid:
                start += 1
            else:
                start = mid
        else:
            end = mid

    return start
##############################################################
N = int(input())
datas = list( map(int, input().split()) )

dp = [ datas[0] ]
dpHistory = [ [[0, datas[0]]] ]

for i, data in enumerate( datas[1:] ):
    if data > dp[-1]: # insert Data
        dp.append( data )
        dpHistory.append( [[i+1, data]] )
    else: # change Data
        index = getInsertIndex( data )
        dp[ index ] = data
        dpHistory[ index ].append( [i+1, data] )
        
# dp : [10, 20, 30, 50]
# dpHistory : [[[0, 10], [2, 10]], [[1, 20], [4, 20]], [[3, 30]], [[5, 50]]]
result = [ 0 for i in range( len(dp) ) ]
beforIndex = 100000000

for index in range( len(dpHistory)-1, -1, -1 ):
    
    for historyIndex in range( len(dpHistory[ index ])-1, -1, -1 ):
        if dpHistory[ index ][ historyIndex ][0] < beforIndex:
            beforIndex = dpHistory[ index ][ historyIndex ][0]
            result[ index ] = dpHistory[ index ][ historyIndex ][1]
            break

print( len(result) )
print( ' '.join(map(str, result ) ) )