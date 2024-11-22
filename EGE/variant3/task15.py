def f(x,a):
    return (((x % 7 != 0 )and (x % 13 == 0)) <= (x > a-40))
for a in range(0, 1000):
    if all(f(x,a) for x in range(1,1000)):
        print(a) 

