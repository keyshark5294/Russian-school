# 15626 РЕШУ ЕГЭ 

# a = {0: "У", 1: "О", 2: "А"}
a = ["У", "О", "А"]
k = 0

for i in range(0, len(a)):
    for j in range(0, len(a)):
        for g in range(0, len(a)):
            for m in range(0, len(a)):
                for n in range(0, len(a)):
                    for l in range(0, len(a)):
                        k += 1
                        if a[i] == 'О' and a[j] == 'У' and a[g] == 'У' and a[m] == 'У' and a[n] == 'О' and a[l] == 'О':
                            print(k)