'''
13298 

Алиса составила все пятибуквенные слова из букв П, Р, И, В, Ы, Ч, К, А,  записала их в алфавитном порядке и пронумеровала. 
После этого Алиса удалила каждое пятое слово и пронумеровала новый список.
Вот начало списка:
1. ААААА
2. ААААВ
3. ААААИ
4. ААААК
5. ААААР (удалилось слово ААААП)

Под каким номером идет первое слово, в котором все буквы различные и согласные?
ВКПРЧ 4946

('В', 'К', 'П', 'Ч', 'Р') 4754
'''


a = sorted('ПРИВЫЧКА')

words = []

for i1 in range(len(a)):
    for i2 in range(len(a)):
        for i3 in range(len(a)):
            for i4 in range(len(a)):
                for i5 in range(len(a)):
                    stroka = a[i1] + a[i2] + a[i3] + a[i4] +a[i5] 
                    words.append(stroka)


for i, sym in enumerate(words):
    if (i+1) % 5 == 0:
        words.pop(i)


for n, word in enumerate(words):
    if 5 == len(set(word)):
        if 'П' in word and 'Р' in word and 'В' in word and 'Ч' in word and 'К' in word:
            print(word)
            print(n+1)
            break

