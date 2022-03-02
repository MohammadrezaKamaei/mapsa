mat1  = [
                [1, 2], 
                [3, 4]
            
        ]

mat2  = [
                [5, 6], 
                [7, 8]
            
        ]
result  = [
                [0, 0], 
                [0, 0]
            
        ]
for i in range(len(mat1)):  
    for j in range(len(mat1[0])):
        print(mat1[i][j])
        print(mat2[i][j])
        result[i][j] = mat1[i][j] + mat2[i][j]

for r in result:
    print(r)
