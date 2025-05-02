# from re import * 

# s = open(r'EGE\24_21421.txt').readline()

# reg = f'[1-9AB][0-9AB]*[02468A]'
# reg = rf'(?=({reg}))'

# m = max((x.group(1) for x in finditer(reg, s)), key=len)
# print(len(m))






# #2518

# s = open('file.txt').readline()

# m = 0 

# for l in range(len(s)):
#     for r in range(l+m, len(s)):
#         c = s[l:r+1]

#         if 'D' not in c:
#             m = max(m, len(c))

#         else: 
#             break

# print(m)





# # 6782
# s = open('file.txt').readline()

# for c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#     s = s.replace(c, 'A')

# for c in '0123456789':
#     s = s.replace(c, '0')


# m = 0 

# for l in range(len(s)):
#     for r in range(l+m, len(s)):
#         c = s[l:r+1]

#         if 'AA' not in c and '00' not in c:
#             m = max(m, len(c))

#         else: 
#             break

# print(m)




#2422

# s = open(r'EGE\24_2422.txt').readline()

# m = 0 

# for l in range(len(s)):
#     for r in range(l+m, len(s)):
#         c = s[l:r+1]

#         if c == ''.join(sorted(c)):
#             m = max(m, len(c))

#         else: 
#             break

# print(m)



# s = open('file.txt').readline()

# m = 0 

# for l in range(len(s)):
#     for r in range(l+m, len(s)):
#         c = s[l:r+1]

#         if all(c[i] + c[i+2] + c[i+3] != c[i+4] + c[i+5] + c[i+6] for i in range(len(c)-5)):
#             m = max(m, len(c))

#         else: 
#             break

# print(m)





#6147 

s = open('file.txt').readline()

m = 10_000

for l in range(len(s)):
    for r in range(l, l+m):
        c = s[l:r+1]

        if c.count('.') == 7:
            m = min(m, len(c))
            break

print(m)