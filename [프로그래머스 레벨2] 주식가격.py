# 스택/큐: 주식가격
def solution(prices):
    stack = []

    answer = [ 0 for i in range(len(prices)) ]
    for i, price in enumerate(prices):
        if stack != [] and stack[-1][0] > price: # 감소하였다면,
            while stack:
                if stack[-1][0] <= price:  break
                popValue, popIndex = stack.pop()
                answer[popIndex] = i - popIndex

        stack.append( [price, i] )
        
    while stack:
        popValue, popIndex = stack.pop()
        answer[popIndex] = i - popIndex
        
    return answer