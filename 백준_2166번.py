# 2166번: 다각형의 면적
# 신발끈 공식 : https://ko.wikipedia.org/wiki/%EC%8B%A0%EB%B0%9C%EB%81%88_%EA%B3%B5%EC%8B%9D
N = int(input())
points = [ [] for i in range(N) ]
for i in range(N):
    points[i] = list( map(int, input().split()) )

a = points[N-1][0] * points[0][1]
b = points[N-1][1] * points[0][0]
for i in range(0, N-1):
    a += points[i][0] * points[i+1][1]
    b += points[i][1] * points[i+1][0]

result = round(abs(a-b)/2, 1)
print(result)