# 1918번: 후위 표기식
befor = input()

weight ={ '*':2,'/':2,'+':1,'-':1,'(':0,')':0 }
after = ""
q=[]

for x in befor:
    # 알파벳 출력
    if x not in weight.keys():
        after += x
        
    #왼쪽 괄호 
    elif x=='(':
        q.append(x)
        
    # 오른쪽 괄호시 왼쪽 괄호 나올때까지 중간 연산자 출력한다 
    elif x==')':
        while q:
            cur=q.pop()
            if cur=='(': break
            after += cur
            
    else:
        # 같은 집합
        # 우선순위가 더 낮다면 이전에 우선순위 높은 연산자를 출력한다 
        while q and q[-1]!='(' and weight[x] <= weight[q[-1]]:
            after += q.pop()
        q.append(x)

# 나머지 연산자를 출력한다 
while q: after += q.pop()
    
print( after )