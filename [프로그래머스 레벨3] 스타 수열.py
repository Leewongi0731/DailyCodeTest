# 월간 코드 챌린지: 스타 수열

def solution(a):
    N = len(a)
    
    datas = {}
    for i, d in enumerate( a ):
        try:
            datas[d].append(i)
        except:
            datas[d] = [i]
            
    answer = 0
    for key in datas.keys():
        if answer < len(datas[key]):
            tmp = 0
            index = 0
            
            for keyIndex in datas[key]:
                if index > keyIndex: continue
                while index < N and a[index]==key:
                    index += 1
                    
                if index < N:
                    tmp += 1
                else:
                    break
                    
                index = max( index+1, keyIndex+1 )
            
            answer = max( answer, tmp )
            
    return answer*2