# 14002번: 가장 긴 증가하는 부분 수열 4

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True, mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return False, start
#############################################
N = int(input())
datas = list(map(int, input().split()))


dp, save = [], []
for i, data in enumerate(datas):
    index = binary_search( data, dp )[1]
    if index >= len(dp):
        dp.append( data )
        save.append( [ [i, data] ] )
    else: # update
        dp[ index ] = data
        save[ index ].append( [i, data] )
        
index, d = save[-1][-1]
result = [ d ]
for i in range( len(save)-2, -1, -1 ):
    for j in range( len(save[i])-1, -1, -1 ):
        if save[ i ][ j ][ 0 ] < index and save[ i ][ j ][ 1 ] < d:
            index = save[ i ][ j ][ 0 ]
            d =  save[ i ][ j ][ 1 ]
            result.append( d )
            break
            
result.reverse()

print( len(result) )
print( ' '.join(map(str, result)) ) 