for x in range(10):
    num1 = x*17**3 + 11*17**2 + 0*17**1 + 9*17**0
    num2 = x*15**3 + 8*15**2 + 14*15**1 + 8*15**0

    if (num1+num2) % 155 == 0:
        print(x)
        print((num1+num2)//155)
        print()

    
