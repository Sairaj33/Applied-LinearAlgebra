def mat1(r,c):  
    mat1 = []
    r = int(input("enter the no of rows for mat1:"))
    c = int(input("enter the no of cols for mat1:"))
    for i in range(r):
        row1 = []
        print("enter the elements of row",i,": ")
        for j in range(c):
            a = int(input())
            row1.append(a)
        mat1.append(row1)
    print(mat1)
    
def mat2(x,y):
        mat2 = []
        x = int(input("enter the no of rows for mat2:"))
        y = int(input("enter the no of cols for mat2:"))
        for i in range(x):
            row2 = []
            print("enter the elements of row",i,": ")
            for j in range(y):
                z = int(input())
                row2.append(z)
            mat2.append(row2)
        print(mat2)  

#addition and Substraction
mat1(r,c)
mat2(x,y)
add = []
sub = []

for i in range(len(row1)):
    add1 = []
    sub1= []
    for j in range(len(row1)):
        add1.append(mat1[i][j] + mat2[i][j])
        sub1.append(mat1[i][j] - mat2[i][j])
    add.append(add1)
    sub.append(sub1)
    
print("ADD:{},Sub:{}".format(add,sub))

#multiplication
mul = []

for i in range(r):
    row=[]
    for j in range(y):
        x=0
        for k in range(c):
            x += (mat1[i][k]* mat2[k][j])
        row.append(x)
    mul.append(row)            
print("Mul:{}".format(mul))
    
    
        
