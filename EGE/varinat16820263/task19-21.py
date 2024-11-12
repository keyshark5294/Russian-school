def f(a, m):
    if m == 0:
        return 0
    
    if a >= 40:
        return m%2==0
    
    
    h = [f(a+1, m-1), f(a+2, m-1)]

    return any(h) if m % 2 != 0 else all(h)

print('19)', [a for a in range(1, 40) if f(a, 2)])
print('20)', [a for a in range(1, 40) if not(f(a, 1)) and f(a, 3)])