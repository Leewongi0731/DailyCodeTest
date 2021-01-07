# 2580번: 스도쿠

def cal(i, j):
    return (i//3)*3 + (j//3)

def sol(n): # 0 <= n <= 80
    if n == 81: # 초과 index -> 앞에 모든 값이 True.
        for s in sudoku:
            print( ' '.join(map(str, s ) ) )
        return True
    
    i = n // 9 # row index
    j = n % 9  # col index
    if sudoku[i][j] != 0: return sol(n+1)
    else:
        for num in range(1, 10): # 사전식으로 앞서는 것을 출력하기 위해, 1~10순서대로 search
            if rowCheck[i][num]==False and colCheck[j][num]==False and boxCheck[cal(i, j)][num]==False:
                # 만약 i, j지점에 해당 num값이 들어갈 수 있고, 이게 최종적으로 정답이 될 수 있다면 -> True
                rowCheck[i][num] = True
                colCheck[j][num]= True
                boxCheck[cal(i, j)][num]= True
                sudoku[i][j] = num
                if sol( n+1 ): return True
                
                
                # i, j지점에 해당 num값이 들어갈 수 있지만, 결과적으로는 옳지 못한 값. -> 다시 Fasle, 0으로 set
                rowCheck[i][num] = False
                colCheck[j][num]= False
                boxCheck[cal(i, j)][num]= False
                sudoku[i][j] = 0
    # i, j지점에 모든 값을 넣을 수 없다면... return False
    return False 
        
####################################################################

sudoku = [ [] for i in range(9) ]
rowCheck = [[False]*10 for i in range(9)]
colCheck = [[False]*10 for i in range(9)]
boxCheck = [[False]*10 for i in range(9)]
for i in range(9):
    sudoku[ i ] = list(map(int, input().split()))
    for j in range(9):        
        # set lowCheck
        rowCheck[i][sudoku[i][j]] = True
        # set colCheck
        colCheck[j][sudoku[i][j]] = True
        # set boxCheck
        boxCheck[cal(i, j)][sudoku[i][j]] = True
sol(0)