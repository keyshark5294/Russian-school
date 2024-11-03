n = int(input())
a = int(input("Введите систему счиления"))
b = ''
while n > 0:
 b = str(n % a) + b
 n = n // a
print(b)