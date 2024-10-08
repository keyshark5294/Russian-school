# Решение когда одна куча 
def f(s, m):
    '''
    s - count stones
    m - count steps
    '''
    if s >= 63:
        return m % 2 == 0 
    
    if m == 0:
        return 0
    
    h = [f(s + 1, m - 1), f(s + 4, m - 1), f(s * 5, m - 1)]

    return any(h) if (m - 1) % 2 == 0 else all(h) 


print('19', [s for s in range(1, 63) if f(s, 2)])
print('20', [s for s in range(1, 63) if not f(s, 1) and f(s, 3)])
print('21', [s for s in range(1, 63) if not f(s, 2) and f(s, 4)])

# Решение когда две кучи
# def f(a, b, m):
#     '''
#     a - count first stones
#     b - count second stones
#     m - count steps
#     '''
    
#     if a + b >= 342:
#         return m % 2 == 0
    
#     if m == 0:
#         return 0 
    
#     h = [f(a + 2, b, m-1), f(a, b+2, m-1), f(a*5, b, m-1), f(a, b*5, m-1)]

#     return any(h) if (m-1) % 2 == 0 else all(h)
#     # return any(h) if (m-1) % 2 == 0 else any(h) для 19 при условии неудочного решения 



# print('19', [s for s in range(1, 326) if f(11, s, 2)])
# print('20', [s for s in range(1, 326) if not f(11, s, 1) and f(11, s, 3)])
# print('21', [s for s in range(1, 326) if not f(11, s, 2) and f(11, s, 4)])