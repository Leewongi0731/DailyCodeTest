# 2018 카카오 공채: 파일명 정렬
import re

def solution(files):
    headFillter = re.compile( "[a-zA-Z -.]+" )
    numberFillter = re.compile( "[0-9]+" )
    datas = []
    for index, file in enumerate( files ):
        head = re.findall( headFillter, file )[0]
        number = re.findall( numberFillter, file )[0]
        datas.append( [head.lower(), int(number), index] )
    
    datas = sorted( datas )
    answer = [ files[ data[2] ] for data in datas ]
    return answer