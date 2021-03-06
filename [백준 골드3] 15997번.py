# 15997번: 승부 예측
# 4팀 참가 => A B / A C / A D / B C / B D / C D -> 총 6경기
# 각 경기의 결과는 이김 / 비김 / 짐 3가지 경우임으로 전체 경우의 수는 3^6
# 각 case의 확률에 따라 점수 부여
import copy

def DFS( idx, score, p ):
    if idx==6: # 모든 게임 종료
        sortScore = [ [s,i] for i, s in enumerate(score) ]
        sortScore = sorted( sortScore, reverse=True ) # socre 내림차순 정렬
        
        # 모든 팀의 승점이 같은 경우 -> 모두 1/2확률로 진출함
        if sortScore[0][0] == sortScore[1][0] == sortScore[2][0] == sortScore[3][0]:
            result[sortScore[0][1]] += p*2/4
            result[sortScore[1][1]] += p*2/4
            result[sortScore[2][1]] += p*2/4
            result[sortScore[3][1]] += p*2/4
            
        # 상위 3팀만 승점이 같음
        elif sortScore[0][0] == sortScore[1][0] == sortScore[2][0]:
            result[sortScore[0][1]] += p*2/3
            result[sortScore[1][1]] += p*2/3
            result[sortScore[2][1]] += p*2/3
            
        # 상위 2팀만 승점이 같음
        elif sortScore[0][0] == sortScore[1][0]:
            result[sortScore[0][1]] += p*2/2
            result[sortScore[1][1]] += p*2/2
        
        # 상위 한팀은 확정, 아래 3개팀의 승점이 같음
        elif sortScore[1][0] == sortScore[2][0] == sortScore[3][0]:
            result[sortScore[0][1]] += p*1
            result[sortScore[1][1]] += p*1/3
            result[sortScore[2][1]] += p*1/3
            result[sortScore[3][1]] += p*1/3
            
        # 상위 한팀은 확정, 아래 2팀만의 승점이 같음
        elif sortScore[1][0] == sortScore[2][0]:
            result[sortScore[0][1]] += p*1
            result[sortScore[1][1]] += p*1/2
            result[sortScore[2][1]] += p*1/2
            
        # 상위 한팀은 확정, 2등도 혼자임
        else:
            result[sortScore[0][1]] += p*1
            result[sortScore[1][1]] += p*1
                    
    else:
        team1Idx= gameList[idx][0]
        team2Idx = gameList[idx][1]
        
        # team1이 승리
        tmpScore = copy.deepcopy( score )
        tmpScore[ team1Idx ] += 3
        DFS( idx+1, tmpScore, p*datas[team1Idx][team2Idx][0] )
        
        # 비김
        tmpScore = copy.deepcopy( score )
        tmpScore[ team1Idx ] += 1
        tmpScore[ team2Idx ] += 1
        DFS( idx+1, tmpScore, p*datas[team1Idx][team2Idx][1] )
        
        # team2가 승리
        tmpScore = copy.deepcopy( score )
        tmpScore[ team2Idx ] += 3
        DFS( idx+1, tmpScore, p*datas[team1Idx][team2Idx][2] )
########################################################################################
countrys = input().split()
gameList = [ (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3) ]
datas = [ [[0,0,0] for i in range(4)] for i in range(4) ] # A->B를 이길 / 비길 / 질 확률
for _ in range(6):
    A,B,W,D,L = input().split()
    W,D,L = float(W), float(D), float(L)
    
    team1Idx = countrys.index( A )
    team2Idx = countrys.index( B )
    datas[team1Idx][team2Idx] = [W, D, L]
    datas[team2Idx][team1Idx] = [L, D, W]

    
result = [0, 0, 0, 0]
DFS(0, [0,0,0,0], 1.0)
for i in range(4): print('%.7f' % result[i])