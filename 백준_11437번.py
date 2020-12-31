# 11437번: LCA
def getParentList(x):
    parentList = [ graph[x] ]
    parent = graph[x]
    while parent != 0:
        parentList.append( graph[parent] )
        parent = graph[parent]
        
    return parentList
########################################################
N = int(input())
link = [ [] for i in range(N+1) ]
for _ in range(N-1):
    link1, link2 = list( map(int, input().split()) )
    link[link1].append( link2 )
    link[link2].append( link1 )
    
childList = [1]
graph = [ [] for i in range(N+1) ]
graph[1] = 0  # parent
while childList:
    parent = childList.pop()
    for child in link[parent]:
        if graph[ child ] != []:
            continue
        
        graph[ child ] = parent
        childList.append( child )
########################################################
M = int(input())
for _ in range(M):
    a, b = list( map(int, input().split()) )
    if a==b:
        print(a)
        continue
        
    # get ParentList
    aParentList = getParentList(a)
    bParentList = getParentList(b)
    
    if len( aParentList ) < len( bParentList ): # 무조건 a가 b보다 lowlevel로 setting
        aParentList, bParentList = bParentList, aParentList
        a, b = b, a

    try:
        aParentList.index(b) # b가 a의 부모라면.
        print( b )
    except:
        aParentList = aParentList[-len(bParentList):]
        
        startIndex = 0
        endIndex = len( aParentList ) - 2
        while startIndex != endIndex:
            nextIndex = (startIndex + endIndex) // 2            
            if aParentList[nextIndex] == bParentList[nextIndex]:
                endIndex = nextIndex
            else:
                if startIndex == nextIndex:
                    startIndex = nextIndex + 1
                else:
                    startIndex  = nextIndex
        result = aParentList[startIndex]
        print(result)