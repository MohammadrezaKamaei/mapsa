def Tafazol (number : int):
    b = number % 10
    c = number // 10
    if c >= b:
        print (c-b)
    else :
        print (b-c)

Tafazol(12)
