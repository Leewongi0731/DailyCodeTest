# 연습문제: 최고의 집합
def solution(n, s):
    # 합이같고, 곱의 최대값은 모든 수가 중앙에 근접한 값을 가질 경우임
    if n > s: return [-1]  # n > s라면 모두 가장 작은 자연수 1로 채워도 불가능하기 때문
    
    if s%n == 0:
        # 나누어 떨어지는 수라면, 나눈 몫으로만 이루어진 집합이 곱의 최대값임
        return [s//n]*n
    else:
        # 나누어 떨어지지 않는다면, 몫으로 채우고, 부족한 값만큼의 원소에 +1하여 합을 채움
        baseVal = s//n
        plusCount = s - (baseVal*n)
        return [baseVal]*(n-plusCount) + [baseVal+1]*plusCount