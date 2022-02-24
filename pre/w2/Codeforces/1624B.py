l1 , l2 , l3 = [int(x) for x in input().split()]

if (l3-l2 == l2 - l1 ):
    print("yes")
elif (abs(l3-l1) % l2 == 0) or (abs(l2-l1) % l3 == 0):
        print("yes")
else :
        print("no")
