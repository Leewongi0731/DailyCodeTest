# 12852번: 1로 만들기 2
N = int(input())
paths = [[N]]
result = 0
try:
    if N == 1:
        result = 0
        r = [1]
        raise r
        
    while True:
        result += 1
        tmp = []
        for path in paths:
            n = path[-1]
            re = [ path + [n-1] ]
            if n % 3 == 0:
                re.append( path + [n//3] )
            if n % 2 == 0:
                re.append( path + [n//2] )

            for r in re:
                if r[-1] == 1:
                    raise r
                tmp.append( r )
        paths = tmp
except:
    print( result )
    print( ' '.join(map(str, r)) )