# 14725번: 개미굴
class Node:
    def __init__(self, data, depth=-1):
        self.data = data
        self.depth = depth
        self.child = {}
        
    def getChild( self, checkData ):
        if checkData in self.child.keys():
            return self.child[checkData]
        return None
    
    def addChild(self, childData):
        child = Node(childData, self.depth+1)
        self.child[childData] = child
        return child        
        
class Graph:
    def __init__( self ):
        self.root = Node("ROOT")
        
    def insertNode(self, datas):
        parent = self.root
        for data in datas:
            tmp = parent.getChild( data )
            if tmp == None: # 존재하지 않는 child인 경우 child 생성
                parent = parent.addChild( data )
            else:
                parent = tmp
                
    def printGraph(self, parent=None):
        if parent==None: parent = self.root
        if parent != self.root: print( '--'*parent.depth + parent.data )
        sortedChild = sorted( parent.child.keys() )
        for childKey in sortedChild:
            self.printGraph( parent.child[childKey] )
################################################################################
N = int(input())
graph = Graph()
for i in range(N):
    datas = input().split()
    graph.insertNode( datas[1:] )
graph.printGraph()