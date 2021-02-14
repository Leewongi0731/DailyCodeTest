# 2020 카카오 인턴쉽: 수식 최대화
from itertools import permutations
import re

def cal( v1, v2, op ):
    if op == '*':
        return v1*v2
    elif op == '+':
        return v1+v2
    elif op=='-':
        return v1-v2

def solution(expression):
    numFiller = re.compile( "[0-9]+" )
    numList = re.findall( numFiller, expression )
    numList = list( map(int, numList) )
    
    opFiller = re.compile("[+*-]+")
    opList = re.findall( opFiller, expression )

    result = -1
    for op in permutations( ["*", "+", "-"], 3 ):
        priority = { 
            op[0] : 0,
            op[1] : 1,
            op[2] : 2
        }
            
        numStack = [numList[0]]
        opStack = []
        for i in range(1, len(numList)):
            while len(opStack) > 0 and priority[ opList[i-1] ] <= priority[ opStack[-1] ]:
                # 지금 연산이 쌓인 연산의 우선순위보다 낮거나 같다면 -> 계산
                v2 = numStack.pop()
                v1 = numStack.pop()

                numStack.append( cal( v1,v2, opStack.pop() ) )

            numStack.append( numList[i] )
            opStack.append( opList[i-1] )
                    
        while opStack:
            v2 = numStack.pop()
            v1 = numStack.pop()

            numStack.append( cal( v1,v2, opStack.pop() ) )
        result = max( result, abs(numStack[-1]) )
    return result