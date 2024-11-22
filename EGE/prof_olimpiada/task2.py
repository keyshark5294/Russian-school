mn = input().split()
m = mn[0]
n = mn[1]
labirint = ''

for _ in range(int(m)):
    stroka = input()
    labirint += stroka+'\n'

labirint = labirint.replace(' ', '').replace('\n', '')

labirint_l = list(labirint)
# print(labirint_l)


'''
H O O O M
O O W O O
O O O O O
O O F O O
'''

def f(start, end):
    if start>end and labirint[start] == 'W':
        return 0
    
    if start == end: 
        return 1
    
    return f(start+1, end)+f(start+2, end)

print(f(labirint.index('H'), labirint.index('F')))
