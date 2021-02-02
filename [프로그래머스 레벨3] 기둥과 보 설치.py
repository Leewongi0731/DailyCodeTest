# 2020 카카오 공채: 기둥과 보 설치
def addPossible( x, y, a, answer):
    if a == 0: # 기둥
        if ( y==0 or       # 바닥 설치거나 
            [x,y-1,0] in answer or    # 아래에 기둥이 있거나
            [x-1,y,1] in answer or    # 왼쪽에 보가 있거나
            [x,y,1] in answer         # 자리에 보가 있거나
           ): return True
    else: # 보
        if ( [x,y-1,0] in answer or   # 아래에 기둥이 있거나
            [x+1,y-1,0] in answer or   # 오른쪽 아래에 기둥이 있거나 
            ( [x-1,y,1] in answer and [x+1,y,1] in answer ) # 왼쪽, 오른쪽에 보가 있거나
           ): return True
        
    return False

def removePossible( x, y, a, answer):
    if a == 0: # 기둥
        # 옆에 기둥이 없고, 양쪽에 보를 지탱할 보가 없다면, 삭제 불가
        if [x,y+1,1] in answer:  # 위에 보가 있을경우 삭제 가능 여부 확인
            if ( 
                [x+1,y,0] not in answer and
                ( [x-1,y+1,1] not in answer or [x+1,y+1,1] not in answer )
               ): return False
        
        if [x-1,y+1,1] in answer:
            if(
                [x-1,y,0] not in answer and
                ( [x-2,y+1,1] not in answer or [x,y+1,1] not in answer )
            ): return False
        
        if [x,y+1,0] in answer:  # 위에 기둥이 있을경우 삭제 가능 여부 확인
            if ( 
                [x-1,y+1,1] not in answer and
                [x,y+1,1] not in answer
            ): return False

    else: # 보
        if [x,y,0] in answer:  # 해당 위치에 기둥이 있다
             if(  
                 [x,y-1,0] not in answer and
                 [x-1,y,1] not in answer
             ): return False

        if [x+1,y,0] in answer: # 오른쪽에 기둥이 있음
            if(
                [x+1,y-1,0] not in answer and
                [x+1,y,1] not in answer
            ): return False

        if [x-1,y,1] in answer: # 왼쪽에 보가 있음
            if(
                [x,y-1,0] not in answer and
                [x-1,y-1,0] not in answer
            ): return False

        if [x+1,y,1] in answer: # 오른쪽에 보가 있음
            if(
                [x+1,y-1,0] not in answer and
                [x+2,y-1,0] not in answer
            ): return False
    
    return True
###########################################################################
def solution(n, build_frame):
    answer = []
        
    for x, y, a, b in build_frame:
        if b ==1 and addPossible( x,y,a,answer ): # 생성
            answer.append( [x,y,a] )
        elif b==0 and removePossible( x,y,a,answer ): # 제거
            answer.remove( [x,y,a] )
            
    answer.sort()
    return answer