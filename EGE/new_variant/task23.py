def f(start, end):
    if start > end or start == 8:
        return 0 
    
    if start == end:
        return 1 
    
    return f(start+1, end) + f(start+2, end) + f(start*2, end)


print(f(3, 14) * f(14, 18))