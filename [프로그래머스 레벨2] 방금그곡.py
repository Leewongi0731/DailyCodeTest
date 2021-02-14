# 2018 카카오 공채: 방금그곡
import math

def solution(m, musicinfos):    
    m = m.replace('C#', 'H')
    m = m.replace('D#', 'I')
    m = m.replace('F#', 'L')
    m = m.replace('G#', 'Z')
    m = m.replace('A#', 'K')
    
    music_data = [ item.split(',') for item in musicinfos ]
    buffer = []
    #하나하나 테스트
    for sTime, eTime, name, melody in music_data:
        sTime = sTime.split(':')
        eTime = eTime.split(':')
        # runtime 
        sTime = int(sTime[0]) * 60 + int(sTime[1])
        eTime = int(eTime[0]) * 60 + int(eTime[1])
        if sTime > eTime:  eTime += 24*60
        runTime = eTime - sTime
  
        melody = melody.replace('C#', 'H')
        melody = melody.replace('D#', 'I')
        melody = melody.replace('F#', 'L')
        melody = melody.replace('G#', 'Z')
        melody = melody.replace('A#', 'K')
        
        melody *= runTime
        melody = melody[:runTime]
        
        if melody.find( m ) != -1:
            buffer.append( [runTime, name] )
    
    #select music
    if len(buffer) == 0: return "(None)"
    else:
        long_music = ""
        long_time = -1
        for music in buffer:
            if music[0] > long_time:
                long_time = music[0]
                long_music = music[1]
    return long_music