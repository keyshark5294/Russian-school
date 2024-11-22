from math import sqrt

def f(start, end):
    if start < end: 
        return 0
    
    if start == end:
        return 1 
    
    return f(start-4, end)+f(start-7, end)+f(int(sqrt(start)), end)

print(f(44, 22)*f(22, 3))