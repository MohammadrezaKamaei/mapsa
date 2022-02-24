l1 , l2 , l3 = [int(x) for x in input().split()]
print (l1)
print (l2)
print (l3)
if (l1 == l2 and l3 % 2 == 0 or l1 == l3 and l2 % 2 == 0 or l2 == l3 and l3 % 2 == 0) or (l1 == l2 + l3 or l2 == l1 + l3 or l3 == l1 + l2):
      print ("YES")
else :
        print("NO")