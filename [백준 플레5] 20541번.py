# 20541번: 앨범정리
import sys

def binary_search(target, data):
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True, mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return False, start

class dictionary:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.underDict = {}
        self.underDictName = []
        self.photo = []
    
    def addPhoto(self, photoName):
        search = binary_search( photoName, self.photo )
        if search[0] == True: # 존재
            print( "duplicated photo name" )
        else:
            self.photo.insert( search[1] ,photoName )
    
    def deletePhoto( self, operation ):
        deletePhotoNum = 0
        try:
            if operation == "-1": # 이름이 사전순으로 가장 빠른 사진을 삭제 합니다
                deletePhotoNum = 1
                self.photo.pop(0)
            elif operation == "1":  # 이름이 사전순으로 가장 늦은 사진을 삭제 합니다. 
                deletePhotoNum = 1
                self.photo.pop()
            elif operation == "0":  # 현재 앨범에 속해있는 모든 사진을 삭제합니다.
                deletePhotoNum = len( self.photo )
                self.photo = []
            else:
                deletePhotoNum = 1
                self.photo.remove( operation )
        except:
            deletePhotoNum = 0
        print( deletePhotoNum )
    
    def addDictonary( self, dictName ):
        search = binary_search( dictName, self.underDictName )
        if search[0] == True: # 존재
            print( "duplicated album name" )
        else:
            newDict = dictionary( self, dictName )
            self.underDict[ dictName ] = newDict
            self.underDictName.insert( search[1] ,dictName )
    
    def deleteDictonary( self, operation ):
        deleteDictNum, deletePhotoNum = 0, 0
        try:
            if operation == "-1": # 이름이 사전순으로 가장 빠른 앨범을 삭제 합니다
                dictName = self.underDictName.pop(0)
                deleteDict = self.underDict.pop(dictName)
                deleteDictNum, deletePhotoNum = deleteDict.deleteMe()
                deleteDictNum += 1
            elif operation == "1":  # 이름이 사전순으로 가장 늦은 앨범을 삭제 합니다. 
                dictName = self.underDictName.pop()
                deleteDict = self.underDict.pop(dictName)
                deleteDictNum, deletePhotoNum = deleteDict.deleteMe()
                deleteDictNum += 1
            elif operation == "0":  # 현재 앨범에 속해있는 모든 앨범을 삭제합니다.
                deleteDictNum = len( self.underDictName )
                for dictName in self.underDictName:
                    tmpDictNum, tmpPhotoNum = self.underDict[ dictName ].deleteMe()
                    deleteDictNum += tmpDictNum
                    deletePhotoNum += tmpPhotoNum
                self.underDictName = []
                self.underDict = {}
            else:
                self.underDictName.remove( operation )
                deleteDict = self.underDict.pop( operation )
                deleteDictNum, deletePhotoNum = deleteDict.deleteMe()
                deleteDictNum += 1
        except:
            deleteDictNum, deletePhotoNum = 0, 0
        print( deleteDictNum, deletePhotoNum )
    
    def deleteMe( self ):
        deleteDictNum, deletePhotoNum  = len( self.underDictName ), len( self.photo )
        for dictName in self.underDictName:
            tmpDictNum, tmpPhotoNum = self.underDict[ dictName ].deleteMe()
            deleteDictNum += tmpDictNum
            deletePhotoNum += tmpPhotoNum
        return deleteDictNum, deletePhotoNum
###############################################################################################################
N = int(input())
now = dictionary( None, "album" )
for _ in range(N):
    op,S = sys.stdin.readline().split()
    
    if op == "mkalb":
        now.addDictonary( S )
    elif op == "rmalb":
        now.deleteDictonary( S )
    elif op == "insert":
        now.addPhoto( S )
    elif op == "delete":
        now.deletePhoto( S )
    elif op == "ca":
        if S == "..":
            if now.parent != None:
                now = now.parent
        elif S == "/":
            while now.parent != None:
                now = now.parent
        else:
            if S in now.underDict.keys():
                now = now.underDict[ S ]
        print( now.name )