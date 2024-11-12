abcd = input().split()
abcd = sorted([int(i) for i in abcd])
e = int(input())

a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])

if 1 <= a <= 1000 and 1 <= b <= 1000 and 1 <= c <= 1000 and 1 <= d <= 1000 and 0 <= e <= 1000:
    all_time = 0
    time = 0
    print(abcd)
    count = 0
    for i in range(1, 6):
        
        try:
            if i % 2 == 0:
                
                print('one')
                print(str(all_time)+'+'+str(a)+'=')
                all_time += a
                print(all_time)
                a += e
                
                
            
            print('two')
            if i % 2 != 0:
                if count == 0:
                    a += e
                    num = max((a, int(abcd[i])))
                    print(str(all_time)+'+'+str(num))
                    all_time += num
                    print(a, int(abcd[i]),  all_time)

                elif count > 0:
                    
                    num = max((a, int(abcd[count-1])))
                    print(a, int(abcd[count-1]))
                    print(str(all_time)+'+'+str(num)+'=')
                    a += e
                    all_time += num
                    print(all_time)
            
            print('count: ', count)
            print('a: ', a)
            print()
            count += 1

        except IndexError:
            pass

print(all_time+1)