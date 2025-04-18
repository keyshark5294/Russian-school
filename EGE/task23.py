# def f(start, end):
#     if start < end or start == 24:
#         return 0 
    
#     if start == end:
#         return 1 
    
#     else:
#         return f(start-2, end) + f(start-3, end) + f(start//4, end)

# print(f(36, 13))


def f(x, y, a, k):
    if x > y or x == 25:
        return 0 
    
    if x == y: 
        if a == 1 and k >= 7:
            return 1
        
        else:
            return 0 
        
    if x == 12:
        a = 1

    return f(x+1, y, a, k+1) + f(x+2, y, a, k+1) + f(x*3, y, a, k+1)


print(f(2, 42, 0, 0))