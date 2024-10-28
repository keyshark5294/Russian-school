# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# x = 0

# if 0 < a <= 10**9 and 0 < b <= 10**9 and 0 < c <= 10**9 and 0 < d <= 10**9:
#     while (a+b) - (c+d+x) > d:
#         x = ((a+b) - (c+d)) - d 
        
#     print(x)

# a, b, c, d = map(int, input().split())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
w = [a, b, c]
w.sort()

df = abs(w[0] + w[1] - w[2])

print(max(0, df - d))