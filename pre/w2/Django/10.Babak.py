msg = "Babak Khorramdin"
print(msg[0])
print(msg[6])
print(msg[0:5])
print(msg[6:16])
print(msg[0:12:2])

a = []
for i in msg:  
    a.append(i)
    if "m" in a:
        print("True")
        break
print(a)
