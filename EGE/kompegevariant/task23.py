def f(start, end):
    if start < end or start == 24:
        return 0 
    
    if start == end:
        return 1 
    
    else:
        return f(start-2, end)+ f(start-3, end) + f(start//4, end)

print(f(36, 13))