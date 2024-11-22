n = int(input())
s = input()
rating = dict()

if 2 <= n <= 1000 and 1 <= len(s) <= 10:
    r_list = []
    c_list = []
    si_list = []

    for i in range(n):
        rating[i] = ''

        si_and_colors = input().split()
        si = si_and_colors[0]
        colors = si_and_colors[1]

        if 1 <= len(si) <= 10 and 1 <= len(colors) <= 10:
            r = len([color for color in colors if color in s])
            c = len(colors)
            r_list.append(r)
            c_list.append(c)
            si_list.append(si)
    
    count1 = 0
    
    for si1, r1, c1 in zip(si_list, r_list, c_list):
        
        count2 = 0
        for si2, r2, c2 in zip(si_list, r_list, c_list):
            
            if count1 == count2:
                continue

            if (r1 > r2) or (r1 == r2 and c1 > c2):
                rating[count1-1] = si1 

            count2 += 1

        count1 += 1
            

in_rating = list(rating.values())
not_in_rating = ' '.join([i for i in si_list if not(i in in_rating) ])
rating[n] = not_in_rating 
result = ' '.join(reversed(list(rating.values())))
result = result.replace('  ', ' ')
print(result)
