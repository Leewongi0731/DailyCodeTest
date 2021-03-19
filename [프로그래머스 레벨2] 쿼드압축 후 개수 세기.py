# 월간 코드 챌린지: 쿼드압축 후 개수 세기
answer = None

def div( arr, i, j, ii, jj ):
    if i==ii and j==jj:
        answer[ arr[i][j] ] += 1
        return arr[i][j]
    else:
        mi, mj = (i+ii)//2, (j+jj)//2
        r1 = div( arr, i, j, mi, mj )
        r2 = div( arr, i, mj+1, mi, jj )
        r3 = div( arr, mi+1, j, ii, mj )
        r4 = div( arr, mi+1, mj+1, ii, jj )
        
        if (r1==0 or r1==1) and (r1==r2==r3==r4):
            answer[r1] -= 3
            return r1
        else:
            return None
        
def solution(arr):
    global answer
    answer = [0, 0]
    n = len(arr)
    div( arr, 0, 0, n-1, n-1 )
    
    return answer