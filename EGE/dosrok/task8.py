a = 'ДГИАШЭ'
k = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:

                    if (a1 != 'И' and a1 != 'А' and a1 != 'Э') and (a5 != 'Д' and a5 != 'Г' and a5 != 'Ш'):
                        k += 1

print(k)