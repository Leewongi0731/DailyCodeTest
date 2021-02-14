# 2019 카카오 공채: 후보키
from itertools import combinations

def beginAddCheck( keyPair, candidateKeySize, candidateKey ):
    for checkNum in range( 1, candidateKeySize ):
        for check in combinations( keyPair, checkNum ):
            # 부분집합 중 이미 candidateKey에 추가된게 있다면 해당 집합은 고려 X
            if check in candidateKey: return False 
    return True
                        
def solution(relation):
    rowN = len(relation)
    colN = len(relation[0])
    
    colIndex = [ i for i in range(colN) ]
    candidateKey = set()
    for candidateKeySize in range( 1, colN+1 ):
        for keyPair in combinations( colIndex, candidateKeySize ):
            # 부분집합 중 candidateKey가 없다면
            if beginAddCheck( keyPair, candidateKeySize, candidateKey ) == True:
                colPair = [ [0 for i in range(candidateKeySize)] for i in range(rowN) ]
                check = set()
                
                for rowIndex in range(rowN):
                    for pairIndex, relationColIndex in enumerate(keyPair):
                        colPair[rowIndex][pairIndex] = relation[rowIndex][relationColIndex]
                    check.add( tuple(colPair[rowIndex]) )
                
                if len(check) == rowN: # 추출된 set의 갯수가 전체의 row의 수와 같다면 -> 유니크 하다!
                    candidateKey.add( keyPair )

    return len(candidateKey)