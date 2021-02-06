# 1141번: 접두사
N = int(input())
datas = [ input() for i in range(N) ]
datas = list(set(datas))
datas = sorted(datas)

result = 1
for i in range( len(datas) - 1 ):
    if datas[i] != datas[i+1][ :len(datas[i]) ]:
        result += 1
print( result )