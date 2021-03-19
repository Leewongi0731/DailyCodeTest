# Summer/Winter Coding: 점프와 순간 이동

# 한 번에 K 칸을 앞으로 점프하거나, (현재까지 온 거리) x 2 에 해당하는 위치로 순간이동
# 앞으로 K 칸을 점프하면 K 만큼의 건전지 사용량이 듭니다
def solution(n):
    ans = 0
    
    while n:
        if n%2 == 1:
            ans += 1
            n -= 1
        # 순간이동(2배)는 cost X
        n //= 2
    
    return ans