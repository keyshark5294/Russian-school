f = open(r'EGE\new_variant\24_21908.txt', 'r').readline() 
m = 0

#'D' * 14
for l in range(len(f)):
    for r in range(l+m, len(f)):
        c = f[l:r]
        print(c)

        if c == 'D' * 14:
            m = max(m, len(f))

        else:
            break

print(m)