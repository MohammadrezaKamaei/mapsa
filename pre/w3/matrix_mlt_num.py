mat1  = [
                [1, 2], 
                [3, 4]
            
        ]
result  = [
                [0, 0], 
                [0, 0]
            
        ]

num = 2

for i in range(len(mat1)): 
    for j in range(len(mat1[0])):
        result[i][j] = num * mat1[i][j]
for r in result:
    print(r)